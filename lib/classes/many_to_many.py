class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            return
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            return
        self._magazine = value

class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        magazines = {article.magazine for article in self.articles()}
        return list(magazines)

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        categories = {article.magazine.category for article in self.articles()}
        return list(categories)

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = {article.author for article in self.articles()}
        return list(authors)

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        if not titles:
            return None
        return titles

    def contributing_authors(self):
        author_article_count = {}
        for article in self.articles():
            author = article.author
            author_article_count[author] = author_article_count.get(author, 0) + 1
        contributing_authors = [author for author, count in author_article_count.items() if count > 2]
        if not contributing_authors:
            return None
        return contributing_authors

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        magazine_article_count = {}
        for article in Article.all:
            magazine = article.magazine
            magazine_article_count[magazine] = magazine_article_count.get(magazine, 0) + 1
        if not magazine_article_count:
            return None
        return max(magazine_article_count, key=lambda mag: magazine_article_count[mag])