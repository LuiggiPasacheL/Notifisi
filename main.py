
from config import *

import schedule
import time

from models.NewsStorage import NewsStorage
from controllers.NewsController import find_news, compare_news
from controllers.TrayController import *

domain = config['page']['domain']
path = config['page']['path']

storage = NewsStorage()

try:
    storage.load_news()
except:
    storage.news = find_news()
    storage.save_news()

schedule.every().day.at(config["time"]).do(compare_news, storage=storage, incoming_news=find_news(domain, path)).tag("review news") # TODO: TAG

icon.run()

while True:
    schedule.run_pending()
    time.sleep(1)
