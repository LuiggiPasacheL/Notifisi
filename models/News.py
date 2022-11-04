

class News:

    def __init__(self, title: str, description: str, link: str):
        self.title = title.strip()
        self.description = description.strip()
        self.link = link.strip()

    def __str__(self):
        return f"""
        title: {self.title}
        description: {self.description}
        link: {self.link}
        """

    def __eq__(self, other):
        if isinstance(other, News):
                return self.title == other.title
        return False


def get_titles(html_parsed):
    titles_tag = html_parsed.find_all('h4', 'mfp_carousel_title')
    titles = list(map(lambda title_tag: title_tag.a.string, titles_tag))
    return titles

def get_descriptions(html_parsed):
    descriptions_tag = html_parsed.find_all('p', 'mfp_carousel_introtext')
    descriptions = list(map(lambda descriptions_tag: descriptions_tag.string, descriptions_tag))
    return descriptions

def get_links(html_parsed, domain):
    titles_tag = html_parsed.find_all('h4', 'mfp_carousel_title')
    links = list(map(lambda title_tag: domain + title_tag.a['href'], titles_tag))
    return links

def create_news_array(titles, descriptions, links):
    total_titles = len(titles)
    total_descriptions = len(descriptions)
    total_links = len(links)
    
    total = 0
    if total_titles == total_descriptions == total_links:
        total = total_titles

    news_array = []
    for news_index in range(total):
        news_array.append(News(titles[news_index], descriptions[news_index], links[news_index]))

    return news_array
