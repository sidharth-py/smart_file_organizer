import os
import shutil
from config import FOLDER_TYPES

def get_category(extension):
    for folder, extensions in FOLDER_TYPES.items():
        if extension.lower() in extensions:
            return folder
    return "Others"

def move_file(file_path, base_directory):
    if not os.path.isfile(file_path):
        return

    filename = os.path.basename(file_path)
    name, extension = os.path.splitext(filename)

    category = get_category(extension)
    target_folder = os.path.join(base_directory, category)

    os.makedirs(target_folder, exist_ok=True)

    target_path = os.path.join(target_folder, filename)

    counter = 1
    while os.path.exists(target_path):
        target_path = os.path.join(
            target_folder,
            f"{name}_{counter}{extension}"
        )
        counter += 1

    shutil.move(file_path, target_path)
    print(f"Moved: {filename} → {category}/")