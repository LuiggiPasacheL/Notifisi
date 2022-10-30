
from bs4 import BeautifulSoup
from news import News

import sqlite3

import requests
import json

with open("config.json", "r") as f:
    config = json.load(f)

domain = config['page']['domain']
path = config['page']['path']

url = domain + path

r = requests.get(url, verify=False)
html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')

titles_tag = soup.find_all('div', 'mfp_carousel_item', 'tns-item')
titles = list(map(lambda title_tag: title_tag.div.h4.a.string, titles_tag))

descriptions_tag = soup.find_all('div', 'mfp_carousel_item', 'tns-item')
descriptions = list(map(lambda descriptions_tag: descriptions_tag.div.p.string, descriptions_tag))

links = list(map(lambda title_tag: domain + title_tag.div.h4.a['href'], titles_tag))

total_news = len(titles)

news = []
for news_index in range(total_news):
    news.append(News(titles[news_index], descriptions[news_index], links[news_index]))

conn = sqlite3.connect(config['database']['name'])

c = conn.cursor()

c.execute(f"""
          CREATE TABLE IF NOT EXISTS {config['database']['table']} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            link TEXT NOT NULL,
            description TEXT NOT NULL
          );
          """)


