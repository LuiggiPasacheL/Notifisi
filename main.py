
from config import *

import schedule
import time
import threading

from models.NewsStorage import NewsStorage
from models.Notifier import notify
from controllers.TrayController import *
from controllers.NewsController import find_news, compare_and_notify_news

domain = config['page']['domain']
path = config['page']['path']

storage = NewsStorage()

try:
    storage.load_news()
except:
    storage.news = find_news(domain, path)
    notify("We found news", f"{len(storage.news)} news founded")
    storage.save_news()

def review_news(domain, path):
    incoming_news = find_news(domain, path)
    schedule.every().day.at(config["time"]).do(compare_and_notify_news, storage=storage, incoming_news=incoming_news).tag("review_news")
    while True:
        schedule.run_pending()
        time.sleep(1)

schedule_thread = threading.Thread(target=review_news, args=(domain, path,), daemon=True)
schedule_thread.start()

# TODO: Execute init views thread here

icon = create_stray(storage)
icon.run()
