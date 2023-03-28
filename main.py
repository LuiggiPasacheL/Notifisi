
from Controller.News_controller import NewsController
from Model.Storage import Storage
from View.systray_view import SystrayView
from config import Config

def main():
    conf = Config()

    systray_view = SystrayView(conf)
    storage = Storage(conf)
    news_controller = NewsController(systray_view, storage)

    news_controller.run()
    news_controller.update_news(auto=True)

if __name__ == '__main__':
    main()
