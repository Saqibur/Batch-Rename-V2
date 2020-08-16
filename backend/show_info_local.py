from config import config
from classes.Anime import Anime
from classes.Episode import Episode
import csv

dataset = csv.reader(open(config.LOCAL_SEARCH_INDEX, 'r', encoding='UTF-8'), delimiter=',')

def search(search_term):
    for row in dataset:
        if "my hero academia" in row[0].lower():
            print(row[3])