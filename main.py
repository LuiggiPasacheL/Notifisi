
import json
import schedule
import time

from models.NewsStorage import NewsStorage
from controllers.NewsController import find_news, compare_news

with open("config.json", "r") as f:
    config = json.load(f)
# TODO: if config file does not exists recreate

domain = config['page']['domain']
path = config['page']['path']

storage = NewsStorage()

try:
    storage.load_news()
except:
    storage.news = find_news()
    storage.save_news()

schedule.every().day.at(config["time"]).do(compare_news, storage=storage, incoming_news=find_news(domain, path)).tag("")

while True:
    schedule.run_pending()
    time.sleep(1)

# print("-----------------------------------------------------")
# print(f"Cantidad de noticias: {len(storage.news)}")
# print(f"Cantidad de noticias nuevas: {count_new_news}")
