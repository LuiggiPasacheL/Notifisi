from Model.Storage import Storage
from Utils.notifier import notify_error, notify_news
from View.systray_view import SystrayView

class NewsController:

    def __init__(self, view: SystrayView, model: Storage) -> None:
        self.model = model
        self.view = view

    def get_news(self):
        if len(self.model.news) == 0 or len(self.model.news) < self.model.conf.displayed_news:
            self.update_news()
        return self.model.news

    def update_news(self, auto=False):
        try:
            self.model.conf.load()
            diff = self.model.update_news()
            self.model.save_news()
            if auto == False:
                notify_news(diff)
            elif diff > 0:
                notify_news(diff)
            self.view.update_menu(self)
        except:
            notify_error("No se pudo sincronizar")
            return []

    def run(self):
        self.view.create_menu(self)
        self.view.run()
