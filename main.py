
from Controller.News_controller import NewsController
from Model.Storage import Storage
from View.systray_view import SystrayView
from config import Config
import schedule

def main():
    conf = Config()

    systray_view = SystrayView(conf)
    storage = Storage(conf)
    news_controller = NewsController(systray_view, storage)

    news_controller.run()
    def update():
        news_controller.update_news()
    try:
        schedule.every().day.at(conf.time).do(update).tag("update_news")
        update()
    except:
        print("No se pudo sincronizar")

if __name__ == '__main__':
    main()
