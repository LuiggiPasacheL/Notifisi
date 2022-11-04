
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
storage.news = incoming_news

storage.save_news()
