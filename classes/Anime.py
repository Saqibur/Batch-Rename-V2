class Anime:
    mal_id = str
    url = str
    image_url = str
    title = str
    airing = bool
    synopsis = str
    _type = str
    episode_count = int
    score = float

    def __init__(self, result_json):
        self.mal_id = result_json["mal_id"]
        self.url = result_json["url"]
        self.image_url = result_json["image_url"]
        self.title = result_json["title"]
        self.airing = result_json["airing"]
        self.synopsis = result_json["synopsis"]
        self._type = result_json["type"]
        self.episodes = result_json["episodes"]
        self.score = result_json["score"]