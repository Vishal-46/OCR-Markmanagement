import os

EXCLUDED = {'.git', '__pycache__', '.venv', '.idea', '.vscode', '.DS_Store'}

def print_tree(path, prefix=""):
    entries = [e for e in os.listdir(path) if e not in EXCLUDED and not e.startswith('.')]
    entries.sort()
    for i, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + entry)
        if os.path.isdir(full_path):
            extension = "    " if i == len(entries) - 1 else "│   "
            print_tree(full_path, prefix + extension)

print_tree(".")
