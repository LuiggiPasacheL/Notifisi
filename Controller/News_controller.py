from Model.Storage import Storage
from Utils.notifier import notify_error, notify_news
from View.systray_view import SystrayView

class NewsController:

    def __init__(self, view: SystrayView, model: Storage) -> None:
        self.model = model
        self.view = view

    def get_news(self):
        if len(self.model.news) == 0:
            self.update_news()
        return self.model.news

    def update_news(self):
        try:
            diff = self.model.update_news()
            self.model.save_news()
            notify_news(diff)
        except:
            notify_error("Error al obtener las noticias")
            return []
        self.view.update_menu(self)

    def run(self):
        self.view.create_menu(self)
        self.view.run()
