from backend import show_info
import json

def search(best_matches=5):
    # best matches = 5 means return the top 5 results.
    search_term = input("Show name: ")
    print("Fetching results, please wait...")
    result = show_info.search(str(search_term), best_matches)

    print("Retrieved: %d shows.\n" % len(result))
    return result
    # for res in result:
    #     print(res.title)

    # anime = result[0]
    # for ep in anime.episodes(anime.mal_id):
    #     print(ep.title)