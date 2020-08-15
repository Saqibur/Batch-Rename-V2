from backend import file_explorer
from config import config
import colorama

### FOR REASONS ###
colorama.init()

def all_files(path=config.TESTING_FOLDER_PATH):
    all_files = file_explorer.all_files_in_path(path)
    print("There are %d files" % len(all_files))
    return all_files
    # for file in all_files:
      #   print(file)