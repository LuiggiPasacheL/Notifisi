
class News:

    def __init__(self, title: str, description: str, link: str):
        self.title = title.title().strip()
        self.description = description.strip()
        self.link = link.strip()

    def get_short_title(self):
        def short_title(title, lenght):
            return title[:lenght-3] + ("..." if len(title) > lenght else "")
        lenght = 40
        return short_title(self.title, lenght)

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "link": self.link
        }

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

    def __hash__(self):
        return hash(self.title)
