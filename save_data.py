
from bs4 import BeautifulSoup

import requests
import json

from models.News import News
from models.NewsStorage import NewsStorage

with open("config.json", "r") as f:
    config = json.load(f)

domain = config['page']['domain']
path = config['page']['path']

url = domain + path

response = requests.get(url, verify=False)
html_doc = response.text

def create_news_array(titles, descriptions, links):
    total_titles = len(titles)
    total_descriptions = len(descriptions)
    total_links = len(links)
    
    total = 0
    if total_titles == total_descriptions == total_links:
        total = total_titles

    news_array = []
    for news_index in range(total):
        news_array.append(News(titles[news_index], descriptions[news_index], links[news_index]))

    return news_array

def get_news(html):
    soup = BeautifulSoup(html, 'html.parser')

    titles_tag = soup.find_all('h4', 'mfp_carousel_title')
    titles = list(map(lambda title_tag: title_tag.a.string, titles_tag))

    descriptions_tag = soup.find_all('p', 'mfp_carousel_introtext')
    descriptions = list(map(lambda descriptions_tag: descriptions_tag.string, descriptions_tag))

    links = list(map(lambda title_tag: domain + title_tag.a['href'], titles_tag))

    incoming_news = create_news_array(titles, descriptions, links)

    return incoming_news

incoming_news = get_news(html_doc)

incoming_news[0].title = "hola que tal"

storage = NewsStorage(incoming_news)

storage.save_news()
