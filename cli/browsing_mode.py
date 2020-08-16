from backend import show_info
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def start():
    while(True):
        top_anime_results = search()

        for i, anime in zip(range(1, len(top_anime_results)),top_anime_results):
            print("[%d] - %s" % (i, anime.title))

        selection = int(input("Select one: "))
        print("You have selected [%d] - %s" % (selection, top_anime_results[selection - 1].title))

        selected_anime = top_anime_results[selection - 1]
        episodes = selected_anime.episodes(selected_anime.mal_id)
        for episode in episodes:
            new_name = "%s %s - %s" % (selected_anime.title, "{:02}".format(episode.id), episode.title)
            print(Fore.GREEN + new_name)

        exit_option = input("Exit? (y/n)")
        if "y" in exit_option.lower():
            exit(0)

def search(best_matches=10):
    # best matches = 5 means return the top 5 results.
    search_term = input("Show name: ")
    print("Fetching results, please wait...")
    result = show_info.search(str(search_term), best_matches)

    print("Retrieved: %d shows.\n" % len(result))
    return result