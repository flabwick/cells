from flask import Flask, render_template, redirect, url_for, jsonify, send_from_directory, abort, send_file, request
from werkzeug.utils import safe_join
from filesystem.loader import FileLoader
from filesystem.folder_loader import FolderTree
from parser.substitution import substitute
from models.cell import Prompt, Cell
import os
import json
from web.routes.chat_route import chat_bp
from urllib.parse import unquote
import tiktoken


app = Flask(__name__)
app.register_blueprint(chat_bp)
loader = FileLoader("files")
tree = FolderTree()

@app.route("/")
def index():
    return redirect(url_for("view_folder", folder_path=""))

@app.route("/folder/<path:folder_path>")
@app.route("/folder/", defaults={"folder_path": ""})
def view_folder(folder_path):
    folder_data = tree.scan(folder_path)
    return render_template("folder.html", folder=folder_data, folder_path=folder_path)

@app.route("/cell/<path:cell_path>")
def show_cell(cell_path):
    full_path = os.path.join("cells", cell_path)
    with open(full_path, "r", encoding="utf-8") as f:
        cdata = json.load(f)

        # Handle list-wrapped cells
        if isinstance(cdata, list) and cdata and isinstance(cdata[0], dict):
            cdata = cdata[0]

        links = cdata.get("links", {})
        prompts = [Prompt(p["title"], p["text"], links) for p in cdata["prompts"]]
        cell = Cell(cdata["name"], prompts)

    return render_template("cell.html", cell=cell, cell_path=cell_path)

@app.route('/images/<path:filename>')
def serve_image(filename):
    search_root = "files/images"
    decoded_filename = unquote(filename)

    # Recursively search for the matching filename
    for root, _, files in os.walk(search_root):
        for file in files:
            if file == decoded_filename:
                full_path = os.path.join(root, file)
                return send_file(full_path)
    
    abort(404)

@app.route("/prompt/<path:cell_path>/<int:pid>")
def show_prompt(cell_path, pid):
    full_path = os.path.join("cells", cell_path)
    with open(full_path, "r", encoding="utf-8") as f:
        cdata = json.load(f)
        links = cdata.get("links", {})
        prompt = cdata["prompts"][pid]
        resolved = substitute(prompt["text"], links, loader)
        return f"<pre style='white-space: pre-wrap'>{resolved}</pre>"

@app.route("/api/resolve/<path:cell_path>/<int:pid>")
def resolve_prompt(cell_path, pid):
    full_path = os.path.join("cells", cell_path)
    errors = []
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            cdata = json.load(f)
            if isinstance(cdata, list) and cdata and isinstance(cdata[0], dict):
                cdata = cdata[0]
            links = cdata.get("links", {})
            prompt = cdata["prompts"][pid]
            text, errors = substitute(prompt["text"], links, loader)
            return jsonify({"text": text, "errors": errors})
    except Exception as e:
        return jsonify({"error": f"Failed to resolve prompt: {str(e)}"}), 500

@app.route("/api/tokencount", methods=["POST"])
def token_count():
    try:
        text = request.json["text"]
        enc = tiktoken.encoding_for_model("gpt-4")
        tokens = len(enc.encode(text))
        return jsonify({"tokens": tokens})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

