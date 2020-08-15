from jikanpy import Jikan
from config import config
from classes.Anime import Anime

def search(search_term: str, best_matches=5) -> dict:
    jikan = Jikan()
    results = jikan.search(
                search_type=config.SEARCH_TYPE,
                query=search_term
            )
    results = results["results"][:best_matches]

    return [ Anime(result) for result in results ]