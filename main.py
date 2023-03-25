
from Controller.News_controller import NewsController

def main():

    news_controller = NewsController()

    news = news_controller.get_news()

    for index, news in enumerate(news):
        print(f"{index + 1}. {news.title}")

    news = news_controller.update_news()

    print("-----------------------------------------------")
    
    for index, news in enumerate(news):
        print(f"{index + 1}. {news.title}")

    news_controller.save_news()

if __name__ == '__main__':
    main()
