import os
import shutil
from pathlib import Path



# Automate file organization
# Automatically sort everything in Downloads folder:
# Move .pdf, .zip, .exe, .jpg files into subfolders (Documents/, Installers/, Images/, etc.).


# Path to Downloads
source_folder = Path.home() / "Downloads"

# Folder categories
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".doc",".txt", ".csv"],
    "Installers": [".exe", ".msi", ".zip"],
    "Videos": [".mp4", ".mov", ".avi"],
}

for file in source_folder.iterdir():
    if file.is_file():
        for folder_name, extensions in file_types.items():
            if file.suffix.lower() in extensions:
                target_folder = source_folder / folder_name
                target_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(target_folder / file.name))
                print(f"Moved: {file.name} → {folder_name}")
                break
