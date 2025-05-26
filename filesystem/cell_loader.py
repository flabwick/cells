import os
import json
from models.cell import Cell, Prompt

class CellLoader:
    def __init__(self, base_dir="data/cells"):
        self.base_dir = base_dir

    def load_all(self):
        cells = []
        for fname in os.listdir(self.base_dir):
            if fname.endswith(".json"):
                with open(os.path.join(self.base_dir, fname), "r", encoding="utf-8") as f:
                    data = json.load(f)
                    links = data.get("links", {})
                    prompts = [Prompt(p["title"], p["text"], links) for p in data["prompts"]]
                    cells.append(Cell(data["name"], prompts))
        return cells
