from cli import check_files
from cli import wiki_tester
from cli import anime_searcher
from cli import renamer

import webbrowser

if __name__ == "__main__":

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