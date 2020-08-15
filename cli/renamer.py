import colorama
import os
import re
from colorama import Fore, Back, Style
from backend.file_explorer import rename_file
import webbrowser
### FOR REASONS ###
colorama.init(autoreset=True)

def show_before_after(anime, all_files):
    episodes = anime.episodes(anime.mal_id)

    print("RENAME DIFFS:")

    new_names = list()

    if (len(all_files) > len(episodes)):
        print("There are extra files in the folder.")
        print("These will be ignored: ")
        for item in all_files[len(episodes):]:
            print(Fore.YELLOW + os.path.basename(item))


    for episode, file_name in zip(episodes, all_files):
        print(Fore.RED + os.path.basename(file_name), end=" -> ")
        new_name = "%s %s - %s" % (anime.title, "{:02}".format(episode.id), episode.title)
        new_names.append(new_name)
        print(Fore.GREEN + new_name)

    print(Fore.BLUE + "=====END OF LIST=====")

def rename_files(selected_anime, all_files):
    episodes = selected_anime.episodes(selected_anime.mal_id)
    for episode, file_name in zip(episodes, all_files):
            new_name = "%s %s - %s" % (selected_anime.title, "{:02}".format(episode.id), episode.title)
            new_name = re.sub(r'[<>:"/\|?*]*', '', new_name)
            rename_file(file_name, new_name)
    print(Fore.BLUE + "=====DONE RENAMING=====")