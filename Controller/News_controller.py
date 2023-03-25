from Model.Storage import Storage

class NewsController:

    def __init__(self) -> None:
        self.storage = Storage()

    def get_news(self):
        return self.storage.news

    def update_news(self):
        news, diff = self.storage.update_news()
        return news

    def save_news(self):
        self.storage.save_news()
