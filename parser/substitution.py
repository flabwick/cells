import re
from filesystem.loader import FileLoader

def substitute(text, link_map, loader: FileLoader):
    """
    Replaces [[1]], [[2]] in text using links, resolves file contents, 
    and preserves brackets while recursively resolving inner file links.
    """
    errors = []

    def replace_numbered(match):
        num = match.group(1)
        path = link_map.get(num)
        if not path:
            return match.group(0)
        try:
            content = loader.read(path)
            if not content.strip():
                errors.append(f"File '{path}' is empty.")
                return match.group(0)
            resolved = resolve_nested(content, loader, errors)
            return f"[[{resolved}]]"
        except FileNotFoundError:
            errors.append(f"File '{path}' not found.")
            return match.group(0)

    resolved_text = re.sub(r"\[\[(\d+)\]\]", replace_numbered, text)
    return resolved_text, errors

def resolve_nested(content, loader: FileLoader, errors):
    """
    Recursively resolves [[path/to/file.md]] inside file content.
    Keeps the brackets: [[file content here]]
    """
    pattern = re.compile(r"\[\[([^\[\]]+)\]\]")

    def replace_file(match):
        path = match.group(1).strip()
        try:
            nested = loader.read(path)
            if not nested.strip():
                errors.append(f"File '{path}' is empty.")
                return match.group(0)
            inner = resolve_nested(nested, loader, errors)
            return f"[[{inner}]]"
        except FileNotFoundError:
            errors.append(f"File '{path}' not found.")
            return match.group(0)

    return pattern.sub(replace_file, content)
