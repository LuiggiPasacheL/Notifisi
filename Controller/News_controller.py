from Model.Storage import Storage
from Utils.notifier import notify_error, notify_news
from View.systray_view import SystrayView

class NewsController:

    def __init__(self, view: SystrayView, model: Storage) -> None:
        self.model = model
        self.view = view

    def create_systray(self):
        self.view.create_menu(self)
        self.view.run()

    def get_news(self):
        return self.model.news

    def update_news(self):
        try:
            news_list, diff = self.model.update_news()
            notify_news(diff)
        except:
            notify_error("Error al obtener las noticias")
            return []
        self.view.update_menu(news_list)
        return news_list

    def save_news(self):
        self.model.save_news()
