
from bs4 import BeautifulSoup
from controllers.NotifyController import notify
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

    try:
        response = requests.get(url, verify=False)
        html = response.text
    except:
        html = None

    return html

def find_news(domain, path):
    html = get_html(domain, path)
    
    try:
        soup = BeautifulSoup(html, 'html.parser')

        titles = get_titles(soup)
        descriptions = get_descriptions(soup)
        links = get_links(soup, domain)

        incoming_news = create_news_array(titles, descriptions, links)
    except:
        notify("Ha ocurrido un error", "Obteniendo las noticias")
        incoming_news = []

    return incoming_news

def renew_and_notify_news(storage, incoming_news):
    if incoming_news:
        count_new_news = storage.renew_news(incoming_news)
        if count_new_news > 0:
            notify("Se encontraron noticias", f"{count_new_news} noticias encontradas")
        notify("No se encontraron noticias", "")
