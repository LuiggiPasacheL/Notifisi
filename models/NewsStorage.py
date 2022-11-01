
class NewsStorage:

    def __init__(self):
        self.news = []

    def get_count_new_news(self, incoming_news) -> int:
        count_news = 0
        for old_news in self.news:
            for new_news in incoming_news:
                if old_news == new_news:
                    return count_news
                else:
                    count_news += 1
        return count_news

    def insert_news(self, incoming_news):
        self.news = incoming_news

    def replace_news(self, quantity, incoming_news):
        for _ in range(quantity):
            self.news.pop()

        for _ in range(quantity):
            self.news.append(incoming_news.pop())

