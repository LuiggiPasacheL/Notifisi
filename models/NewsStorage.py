from config import *

import pickle

class NewsStorage:

    def __init__(self):
        self.name_file = config['file']
        self.news = []

    def insert_news(self, incoming_news):
        self.news = incoming_news

    def get_count_new_news(self, incoming_news) -> int:
        count_news = 0
        last_save_news = self.news[0]

        for new_news in incoming_news:
            if last_save_news == new_news:
                return count_news
            else:
                count_news += 1

        return count_news

    def replace_news(self, quantity, incoming_news):
        for _ in range(quantity):
            self.news.pop()
        
        for index in reversed(range(quantity)):
            self.news.insert(0, incoming_news[index])

    def save_news(self):
        with open(self.name_file, 'wb') as save_file:
            pickle.dump(self.news, save_file, pickle.HIGHEST_PROTOCOL)

    def load_news(self):
        with open(self.name_file, 'rb') as load_file:
            self.news = pickle.load(load_file)

    def renew_news(self, incoming_news):
        new_news = self.get_count_new_news(incoming_news)

        if new_news > 0:
            self.replace_news(new_news, incoming_news)
            self.save_news()
            
        return new_news

