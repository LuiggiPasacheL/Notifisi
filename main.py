
from Controller.News_controller import NewsController
from Model.Storage import Storage
from View.systray_view import SystrayView

def main():

    systray_view = SystrayView()
    storage = Storage()
    news_controller = NewsController(systray_view, storage)
    news_controller.create_systray()
    news_controller.update_news()
    news_controller.save_news()

if __name__ == '__main__':
    main()

