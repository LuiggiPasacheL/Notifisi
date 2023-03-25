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
        incoming_news = incoming_news[0:5]

        diff = len(set(incoming_news) - set(self.news))
        if len(self.news) == 0:
            self.news = incoming_news
        else:
            diff_news = incoming_news[0:diff]
            diff_news = diff_news[::-1]

            self.news = self.news[::-1]
            self.news.extend(diff_news)
            self.news = self.news[::-1]

            for _ in range(diff):
                self.news.pop()

        return self.news, diff 

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
            result.append(News(title, description, link))

        return result

    def __get_info(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        titles_tag = soup.find_all('h4', 'mfp_carousel_title')
        descriptions_tag = soup.find_all('p', 'mfp_carousel_introtext') 

        titles = list(map(lambda title_tag: title_tag.a.string, titles_tag))
        descriptions = list(map(lambda descriptions_tag: descriptions_tag.string, descriptions_tag))
        links = list(map(lambda title_tag: self.conf.domain + title_tag.a['href'], titles_tag))

        return titles, descriptions, links

