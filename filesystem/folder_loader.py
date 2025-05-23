import os
import json
from models.cell import Cell, Prompt

class FolderTree:
    def __init__(self, root_path="cells"):
        self.root = root_path

    def scan(self, subpath=""):
        full = os.path.join(self.root, subpath)
        entries = os.listdir(full)
        folders = []
        cells = []

        for e in entries:
            ep = os.path.join(full, e)
            if os.path.isdir(ep):
                folders.append({
                    "name": f"📁 {e}",
                    "path": os.path.join(subpath, e)
                })
            elif e.endswith(".json"):
                with open(ep, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # if the root JSON is a list, use first item's name
                    if isinstance(data, list) and data and isinstance(data[0], dict):
                        name = data[0].get("name", e)
                    elif isinstance(data, dict):
                        name = data.get("name", e)
                    else:
                        name = e  # fallback to filename

                    cells.append({
                        "name": f"🧩 {name}",
                        "path": os.path.join(subpath, e)
                    })
        return {"folders": sorted(folders, key=lambda x: x["name"]),
                "cells": sorted(cells, key=lambda x: x["name"]),
                "name": f"📁 {subpath or 'Root'}"}
