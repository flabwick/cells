import sys
from filesystem.loader import FileLoader
from models.folder import Folder
from models.cell import Cell, Prompt
from ui.navigator import Navigator
from filesystem.cell_loader import CellLoader

def build_structure(loader):
    cell_loader = CellLoader()
    cells = cell_loader.load_all()
    return [Folder(name="Default Folder", cells=cells)]

def main():
    loader = FileLoader("files")
    folders = build_structure(loader)
    navigator = Navigator(folders, loader)
    try:
        navigator.start()
    except (KeyboardInterrupt, EOFError):
        sys.exit()

if __name__ == "__main__":
    main()
