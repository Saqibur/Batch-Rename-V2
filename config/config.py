TESTING_FOLDER_PATH = "./data/Anime/"
SEARCH_TYPE = "anime"
WELCOME_MESSAGE = """
+--------------------------------------------------------------------+
|                                                                    |
|  WELCOME TO BATCH-RENAME-V2      XXXXXXXX   XXXXXXX   XXXXXX       |
|  RENAME ANIME FILES              XX     XX  XX    XX  X     X      |
|  THIS IS AN ALPHA RELEASE        XX     XX  XX   XX   X    XX      |
|  THINGS WILL BREAK               XXXXXXXX   XXXXXX       XXX       |
|  BE CAREFUL                      XX     XX  XX XXX     XXX         |
|                                  XX    XXX  XX   XX   X            |
| +---------------------------+    XXXXXXXX   XX    XX  XXXXXXXX     |
|                                                                    |
+--------------------------------------------------------------------+

+---------------------------+
|                           |
| FEATURES:                 |
| - MAL searching           |
| | Auto folder rename      |
| | Episode numbers         |
| - Episode titles          |
|                           |
+---------------------------+
"""
from datetime import datetime
LOG_FILE = './Logs/%s-logs.txt' % datetime.now().strftime("%Y-%m-%d %H-%M-%S")
LOG_FOLDER = './Logs'