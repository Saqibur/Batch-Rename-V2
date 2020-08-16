import os
import logging

def all_files_in_path(path: str) -> list:
    logging.info("Looking for files.")
    if path is None:
        logging.info("Invalid Path.")
        print("Invalid path provided.")
        return
    if not os.path.isdir(path):
        logging.info("Invalid directory.")
        print("Not a valid directory")
        return

    all_files_in_folder = list()
    root = path
    for path, subdirectories, files in os.walk(root):
        for name in files:
            all_files_in_folder.append(os.path.join(path, name))
            logging.info("Found file: %s" % name)

    return all_files_in_folder

def rename_file(path, new_name):
    logging.info("Started file renames.")
    basename = os.path.basename(path)
    extention = os.path.splitext(path)
    os.rename(path, path.split(basename)[0] + new_name + extention[1])
    logging.info("Renamed %s to %s" % (basename, new_name))
