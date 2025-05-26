import os
import json
import shutil
import sys

TEMPLATE_DIR = os.path.dirname(__file__)
FILES_ROOT = os.path.abspath(os.path.join(TEMPLATE_DIR, "..", "files"))

def load_templates():
    with open(os.path.join(TEMPLATE_DIR, 'templates.json'), 'r') as f:
        return json.load(f)

def get_markdown_path():
    if len(sys.argv) >= 2:
        path = sys.argv[1].strip('"\'')
    else:
        path = input("Enter path to the markdown file: ").strip('"\'')
    abs_path = os.path.abspath(path)
    if not abs_path.startswith(FILES_ROOT) or not os.path.isfile(abs_path):
        print("Invalid or unauthorized file path.")
        sys.exit(1)
    return abs_path

def process_cell_file(cell_path):
    with open(cell_path, 'r') as f:
        cell = json.load(f)

    cell_name = cell.get("name", "unnamed_cell")
    base_dir = os.path.dirname(cell_path)
    output_dir = os.path.join(base_dir, f"{cell_name}_generated")
    os.makedirs(output_dir, exist_ok=True)

    # Load and map linked content
    link_contents = {}
    for key, relative_path in cell["links"].items():
        full_path = os.path.abspath(os.path.join(FILES_ROOT, relative_path))
        if not os.path.isfile(full_path):
            print(f"Missing link target: {relative_path}")
            sys.exit(1)
        with open(full_path, 'r') as lf:
            link_contents[key] = lf.read()

    # Write each prompt as a separate .md file
    for prompt in cell["prompts"]:
        title = prompt["title"].replace(" ", "_")
        text = prompt["text"]
        for key, content in link_contents.items():
            text = text.replace(f"[[{key}]]", content)
        with open(os.path.join(output_dir, f"{title}.md"), 'w') as out_file:
            out_file.write(text)

    print(f"Generated cell prompts to: {output_dir}")

def apply_template(md_path, template_name, templates):
    if template_name not in templates:
        print("Template not found.")
        sys.exit(1)

    base_name = os.path.splitext(os.path.basename(md_path))[0]
    target_dir = os.path.join(os.path.dirname(md_path), base_name)
    os.makedirs(target_dir, exist_ok=True)

    with open(md_path, 'r') as f:
        original_content = f.read()

    template = templates[template_name]
    original_preserved = any(
        isinstance(content, str) and "{{original_content}}" in content
        for content in template.values()
    )

    if not original_preserved:
        print("ERROR: Template does not preserve original content. Aborting.")
        sys.exit(1)

    def create_structure(base, structure):
        for name, content in structure.items():
            path = os.path.join(base, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_structure(path, content)
            else:
                file_content = content.replace("{{markdown_filename}}", os.path.basename(md_path))
                file_content = file_content.replace("{{original_content}}", original_content)
                with open(path, 'w') as f:
                    f.write(file_content)

    create_structure(target_dir, template)

    try:
        os.remove(md_path)
    except Exception as e:
        print(f"Warning: Failed to delete original file: {e}")

def main():
    path = get_markdown_path()
    if path.endswith(".cell.json"):
        process_cell_file(path)
    else:
        templates = load_templates()
        keys = list(templates.keys())
        print("Available templates:")
        for idx, key in enumerate(keys, start=1):
            print(f"{idx}. {key}")
        selected_idx = input("Choose a template number: ").strip()
        if not selected_idx.isdigit() or not (1 <= int(selected_idx) <= len(keys)):
            print("Invalid selection.")
            sys.exit(1)
        selected_template = keys[int(selected_idx) - 1]
        apply_template(path, selected_template, templates)

if __name__ == "__main__":
    main()
