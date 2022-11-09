
import config

import schedule
import time
import threading

from models.NewsStorage import NewsStorage
from models.Notifier import notify
from controllers.SystrayController import create_systray
from controllers.NewsController import find_news, renew_and_notify_news

if __name__ == "__main__":
    storage = NewsStorage()

    try:
        storage.load_news()
    except:
        storage.insert_news(find_news(config.domain, config.path))
        storage.save_news()
        notify("Se encontraron noticias", f"{len(storage.news)} noticias encontradas")

    def review_news(domain, path):
        incoming_news = find_news(domain, path)
        try:
            schedule.every().day.at(config.time).do(renew_and_notify_news,storage=storage, incoming_news=incoming_news).tag("renew_news")
        except schedule.ScheduleValueError:
             schedule.every().day.do(renew_and_notify_news,storage=storage, incoming_news=incoming_news).tag("renew_news")
        while True:
            schedule.run_pending()
            time.sleep(1)

    schedule_thread = threading.Thread(target=review_news, args=(config.domain, config.path,), daemon=True)
    schedule_thread.start()

    icon = create_systray(storage)
    icon.run()
