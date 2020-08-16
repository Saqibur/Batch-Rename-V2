import urllib
import logging
import urllib.error

def internet_on():
    print("Checking your internet connection.")
    try:
        urllib.request.urlopen('https://myanimelist.net/', timeout=2)
        return True
    except urllib.error.URLError as err:
        logging.error(err)
        return False