from parser.substitution import substitute
from ui.clipboard import copy

class CellViewer:
    def __init__(self, cell, loader):
        self.cell = cell
        self.loader = loader

    def show(self):
        while True:
            print(f"\nCell: {self.cell.name}")
            for i, p in enumerate(self.cell.prompts, 1):
                print(f"{i}. {p.title}")
            print("0. Back")
            choice = input("Select prompt: ").strip()
            if choice == "0":
                return
            if choice.isdigit() and 1 <= int(choice) <= len(self.cell.prompts):
                prompt = self.cell.prompts[int(choice)-1]
                resolved = substitute(prompt.text, prompt.links, self.loader)
                copy(resolved)
                print("Prompt copied to clipboard.")
            else:
                print("Invalid choice.")
