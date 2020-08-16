# Batch-Rename-V2

A simple batch renamer for several files/folder structures. Can be used through a CLI or GUI.

Yes it's for anime.

<img height="200px" src="https://www.pngkit.com/png/detail/294-2943980_7639058-thumbs-up-anime-meme.png">


## Build from scratch?
```bash
    $ pip install -r requirements.txt
    $ pyinstaller main.py --distpath dist --clean --onefile -n batch-rename-v2
    # OR
    $ pyinstaller main.py --distpath dist --clean --onedir -n batch-rename-v2
    # To run:
    $ dist/batch-rename-v2
```

## Doing
- Add cover image from MAL.
- Add mode explanations.
- Create the following modes:
1. Browse only-mode.
2. Option to create a new folder and files instead of renaming.

---- FIRST MILESTONE ----

## TODO
- Remove all the wikipedia stuff
- Create persistent CLI.
- The so-called function approach has a problem i need to fix. Right now, it needs to get evaluated every time. I don't want that.
- Integrate wikipedia search. Not really important because the results from MAL are promising.
- Write updates scripts for full reseed and reindex of anime episode database.
- Start GUI work.

## Done
- ~Add internet connection checks.~
- ~Added logging in case someone decides to actually report an error.~
- ~Implement Jikan Parser.~
- ~Parse anime episode data from Wikipedia.~
- ~Created primary data source for anime episodes...phew.~
- ~Create local index of all anime episodes.~

## Episode Sources
- We now have two sources.
- JikanPy: Which pulls from MyAnimeList
- Wikipedia

Offering a choice between these two is cool. For me, I preferred the Wikipedia ones, which is why the first one to get implemented is the Wikipedia one.

However, the JikanPy one is more complete, stays up to date, and is the perfect API for on the fly renames.

## Features
- I quickly realized that, rather than querying episode names or lists from wikipedia each time we run this app, it would be better to save a local copy inside some kind of csv. Not only is this more considerate with Wikimedia's API, we can just run a sync every now and then and we're good to go. I could even add a verify script which makes sure we have the latest corrections.
- I might still keep the wikipedia searcher, just for the sake of completeness.
- You should be able to auto-rename an entire series using the titles from Wikipedia.

# Me 6 Hours into this dumb project ->
<img src="https://i.ytimg.com/vi/jtTBYMvLBbw/maxresdefault.jpg">