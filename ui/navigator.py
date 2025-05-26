from ui.cell_viewer import CellViewer

class Navigator:
    def __init__(self, folders, loader):
        self.folders = folders
        self.loader = loader

    def start(self):
        while True:
            print("\nFolders:")
            for i, f in enumerate(self.folders, 1):
                print(f"{i}. {f.name}")
            print("0. Exit")
            choice = input("Select folder: ").strip()
            if choice == "0":
                break
            if choice.isdigit() and 1 <= int(choice) <= len(self.folders):
                self._open_folder(self.folders[int(choice)-1])
            else:
                print("Invalid choice.")

    def _open_folder(self, folder):
        while True:
            print(f"\nFolder: {folder.name}")
            for i, c in enumerate(folder.cells, 1):
                print(f"{i}. {c.name}")
            print("0. Back")
            choice = input("Select cell: ").strip()
            if choice == "0":
                return
            if choice.isdigit() and 1 <= int(choice) <= len(folder.cells):
                viewer = CellViewer(folder.cells[int(choice)-1], self.loader)
                viewer.show()
            else:
                print("Invalid choice.")
