

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

