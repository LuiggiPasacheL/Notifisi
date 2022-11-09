
import config

import schedule
import time
import threading

from models.NewsStorage import NewsStorage
from controllers.NotifyController import notify
from controllers.SystrayController import create_systray
from controllers.NewsController import find_news, renew_and_notify_news

def review_news():
    incoming_news = find_news(config.domain, config.path)
    try:
        schedule.every().day.at(config.time).do(renew_and_notify_news,storage=storage, incoming_news=incoming_news).tag("renew_news")
    except schedule.ScheduleValueError:
         schedule.every().day.do(renew_and_notify_news,storage=storage, incoming_news=incoming_news).tag("renew_news")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    storage = NewsStorage()

    try:
        storage.load_news()
    except:
        storage.insert_news(find_news(config.domain, config.path))
        storage.save_news()
        notify("Se encontraron noticias", f"{len(storage.news)} noticias encontradas")

    schedule_thread = threading.Thread(target=review_news, daemon=True)
    schedule_thread.start()

    icon = create_systray(storage)
    icon.run()
