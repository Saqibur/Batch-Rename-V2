from jikanpy import Jikan
from config import config
from classes.Anime import Anime
from classes.Episode import Episode

def __set_anime_episodes(anime_id: int) -> list:
    print("Fetching episode lists for: %d" % anime_id)

    jikan = Jikan()
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

def search(search_term: str, best_matches=5) -> dict:
    jikan = Jikan()
    results = jikan.search(
                search_type=config.SEARCH_TYPE,
                query=search_term
            )
    results = results["results"][:best_matches]

    retrieved_anime = list()

    for result in results:
        anime = Anime(result)
        anime.episodes = __set_anime_episodes
        retrieved_anime.append(anime)

    return retrieved_anime