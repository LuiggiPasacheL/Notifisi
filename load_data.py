
from models.NewsStorage import NewsStorage

storage = NewsStorage()
storage.load_news()

print(storage.news[0], storage.news[-1])
