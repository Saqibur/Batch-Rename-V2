from cli import check_files
from cli import wiki_tester
from cli import anime_searcher
from cli import renamer
from config import config
from backend import network
import logging
import webbrowser
import os

if __name__ == "__main__":

    if network.internet_on() is not True:
        print("Cannot connect to MAL.net, please check your internet connection.")
        exit(0)

    if config.USE_LOCAL:
        if os.path.isdir(config.LOG_FOLDER) is not True:
            os.mkdir(config.LOG_FOLDER)

        if os.path.exists(config.LOCAL_SEARCH_INDEX) is not True:
            print("Downloading local search index. Please wait.")
            print("It's a one time download for a big file.")
            import urllib.request
            with urllib.request.urlopen(config.DOWNLOAD_LINK_LOCAL_SEARCH_INDEX) as f:
                try:
                    os.mkdir(config.LOCAL_SEARCH_INDEX_FOLDER)
                except:
                    print("Folder already exists")
                open(config.LOCAL_SEARCH_INDEX, 'wb+').write(f.read())

    logging.basicConfig(
        filename=config.LOG_FILE,
        filemode='w+',
        format='%(asctime)s.%(msecs)03d %(levelname)s - %(message)s',
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    logging.info("Application Started")
    print(config.WELCOME_MESSAGE)
    path_to_anime = str(input("Path to folder: "))
    all_files = check_files.all_files(path_to_anime)
    # wiki_tester.test()
    top_anime_results = anime_searcher.search()
    for i, anime in zip(range(1, len(top_anime_results)),top_anime_results):
        print("[%d] - %s" % (i, anime.title))
    selection = int(input("Select one: "))

    print("You have selected [%d] - %s" % (selection, top_anime_results[selection - 1].title))

    selected_anime = top_anime_results[selection - 1]

    renamer.show_before_after(selected_anime, all_files)

    confirmation = str(input("Do you want to rename your files? (y/n) ")).lower()
    if confirmation == "y":
        print("Changing file names")
        renamer.rename_files(selected_anime, all_files)
        webbrowser.open(path_to_anime)
    else:
        print("Not changing anything. Exiting now.")