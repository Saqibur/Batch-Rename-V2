import os
def all_files_in_path(path: str) -> list:
    if path is None:
        print("Invalid path provided.")
        return
    if not os.path.isdir(path):
        print("Not a valid directory")
        return

    all_files_in_folder = list()
    root = path
    for path, subdirectories, files in os.walk(root):
        for name in files:
            all_files_in_folder.append(os.path.join(path, name))

    return all_files_in_folder

def rename_file(path, new_name):
    basename = os.path.basename(path)
    extention = os.path.splitext(path)
    os.rename(path, path.split(basename)[0] + new_name + extention[1])