import os
import re

class FileLoader:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def read(self, relative_path):
        full_path = os.path.join(self.base_dir, relative_path)

        # Try default path
        if os.path.isfile(full_path):
            with open(full_path, 'r', encoding='utf-8') as f:
                return f.read()

        # Try with .md extension if not present
        if not full_path.endswith(".md") and os.path.isfile(full_path + ".md"):
            with open(full_path + ".md", 'r', encoding='utf-8') as f:
                return f.read()

        raise FileNotFoundError(f"File '{relative_path}' not found.")

