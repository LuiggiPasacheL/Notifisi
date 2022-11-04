
from bs4 import BeautifulSoup

import requests
import json

from models.News import get_links, get_descriptions, get_titles, create_news_array
from models.NewsStorage import NewsStorage
from models.Notifier import notify

def get_html(domain, path):
    url = domain + path

    response = requests.get(url, verify=False)
    html = response.text

    return html

with open("config.json", "r") as f:
    config = json.load(f)
# TODO: if config file does not exists recreate

domain = config['page']['domain']
path = config['page']['path']

html = get_html(domain, path)
soup = BeautifulSoup(html, 'html.parser')

titles = get_titles(soup)
descriptions = get_descriptions(soup)
links = get_links(soup, domain)

incoming_news = create_news_array(titles, descriptions, links)

storage = NewsStorage()

try:
    storage.load_news()
except:
    storage.news = incoming_news
    storage.save_news()

# begin of event to schedule
def find_news():
    # TODO: Avoid duplicate code
    html = get_html(domain, path)
    soup = BeautifulSoup(html, 'html.parser')

    titles = get_titles(soup)
    descriptions = get_descriptions(soup)
    links = get_links(soup, domain)

    incoming_news = create_news_array(titles, descriptions, links)
    # Duplicate

    count_new_news = storage.get_count_new_news(incoming_news)

    if count_new_news == 0:
        storage.replace_news(count_new_news, incoming_news)
        storage.save_news()
        notify("We found news", f"{count_new_news} news founded")

# end of event

import schedule
import time

schedule.every().day.at(config["time"]).do(find_news)

while True:
    schedule.run_pending()
    time.sleep(1)


# print("-----------------------------------------------------")
# print(f"Cantidad de noticias: {len(storage.news)}")
# print(f"Cantidad de noticias nuevas: {count_new_news}")
