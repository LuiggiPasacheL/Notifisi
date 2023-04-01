import json
import requests
from bs4 import BeautifulSoup
from .News import News
from config import Config

class Storage:

    def __init__(self, config: Config) -> None:
        self.conf = config
        try:
            with open(self.conf.data_path, "r") as json_file:
                self.news = [
                        News(obj["title"], obj["description"], obj["link"]) 
                        for obj in json.load(json_file)
                    ]
        except:
            self.news = []

    def update_news(self):
        incoming_news = self.__load_news()
        incoming_news = incoming_news[0:self.conf.displayed_news]

        diff = len(set(incoming_news) - set(self.news))
        self.news = incoming_news
        return diff 

    def save_news(self):
        news_dict_list = [news.to_dict() for news in self.news]
        with open(self.conf.data_path, "w") as json_file:
            json.dump(news_dict_list, json_file)

    def __get_response(self):
        return requests.get(self.conf.url, verify=False, timeout=10)

    def __load_news(self):
        response = self.__get_response()

        html = response.text
        titles, descriptions, links = self.__get_info(html)

        return self.__create_news(titles, descriptions, links)

    def __create_news(self, titles, descriptions, links):
        result = []

        for title, description, link in zip(titles, descriptions, links):
            news = News(title, description, self.__complete_link(link))
            result.append(news)

        return result

    def __complete_link(self, link):
        link_striped = link.strip()
        if not self.conf.domain in link_striped:
            return self.conf.domain + link_striped
        else:
            return link_striped

    def __get_info(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        news_tags = soup.select(self.conf.queryselectors['cards'])

        titles = [ news_tag.select_one(self.conf.queryselectors['titles']).get_text() for news_tag in news_tags ]
        descriptions = [ news_tag.select_one(self.conf.queryselectors['descriptions']).get_text() for news_tag in news_tags ]
        links = [ news_tag.select_one(self.conf.queryselectors['links'])['href'] for news_tag in news_tags ]

        return titles, descriptions, links


