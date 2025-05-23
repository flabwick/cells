from flask import Blueprint, render_template, request, jsonify
import uuid
from chat.api import send, list_chats, load_chat

chat_bp = Blueprint("chat", __name__, template_folder="../templates")

@chat_bp.route("/chat")
def chat_home():
    return render_template("chat.html")

@chat_bp.route("/chat/send", methods=["POST"])
def chat_send():
    data = request.json
    response = send.process_message(data["chat_id"], data["message"])
    return jsonify(response)

@chat_bp.route("/chat/list", methods=["GET"])
def chat_list():
    return jsonify(list_chats.get_chat_summaries())

@chat_bp.route("/chat/load/<chat_id>", methods=["GET"])
def chat_load(chat_id):
    return jsonify(load_chat.get_chat(chat_id))
@chat_bp.route("/chat/delete/<chat_id>", methods=["DELETE"])
def chat_delete(chat_id):
    import os
    path = f"files/chat_sessions/{chat_id}.json"
    if os.path.exists(path):
        os.remove(path)
    return jsonify({"status": "deleted"})
