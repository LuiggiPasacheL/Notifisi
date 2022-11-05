
from bs4 import BeautifulSoup
from models.Notifier import notify
from models.News import News
import requests

def get_titles(html_parsed):
    titles_tag = html_parsed.find_all('h4', 'mfp_carousel_title')
    titles = list(map(lambda title_tag: title_tag.a.string, titles_tag))
    return titles

def get_descriptions(html_parsed):
    descriptions_tag = html_parsed.find_all('p', 'mfp_carousel_introtext')
    descriptions = list(map(lambda descriptions_tag: descriptions_tag.string, descriptions_tag))
    return descriptions

def get_links(html_parsed, domain):
    titles_tag = html_parsed.find_all('h4', 'mfp_carousel_title')
    links = list(map(lambda title_tag: domain + title_tag.a['href'], titles_tag))
    return links

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

def get_html(domain, path):
    url = domain + path

    response = requests.get(url, verify=False)
    html = response.text

    return html

def find_news(domain, path):
    html = get_html(domain, path)
    soup = BeautifulSoup(html, 'html.parser')

    titles = get_titles(soup)
    descriptions = get_descriptions(soup)
    links = get_links(soup, domain)

    incoming_news = create_news_array(titles, descriptions, links)

    return incoming_news

def compare_and_notify_news(storage, incoming_news):
    count_new_news = storage.get_count_new_news(incoming_news)

    if count_new_news > 0:
        storage.replace_news(count_new_news, incoming_news)
        storage.save_news()
        notify("We found news", f"{count_new_news} news founded")
    notify("No news found", "")
