from jikanpy import Jikan
from config import config
from classes.Anime import Anime
from classes.Episode import Episode
from jikanpy.exceptions import APIException

def __set_anime_episodes(anime_id: int) -> list:
    print("Fetching episode lists for: %d" % anime_id)

    jikan = Jikan()
    try:
        anime_with_episodes = jikan.anime(anime_id, extension='episodes')['episodes']
        episodes = []

        for ep in anime_with_episodes:
            episodes.append(
                Episode(
                    ep['episode_id'],
                    ep['title'],
                )
            )

        return episodes
    except APIException:
        print("Failed to retrieve and connect to MAL.")
        print("Please close the app and try again later")
    except:
        print("SOMETHING WENT REALLY BAD")

def search(search_term: str, best_matches=5) -> dict:
    jikan = Jikan()
    try:
        results = jikan.search(
                    search_type=config.SEARCH_TYPE,
                    query=search_term
                )
    except APIException:
        print("Failed to retrieve and connect to MAL.")
    except:
        print("Something went horribly wrong. You should probably close the application. Lol.")

    results = results["results"][:best_matches]

    retrieved_anime = list()

    for result in results:
        anime = Anime(result)
        anime.episodes = __set_anime_episodes
        retrieved_anime.append(anime)

    return retrieved_anime