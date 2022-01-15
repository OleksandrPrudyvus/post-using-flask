"""
Module contains class Tag for DB.

Classes:
    Tag(db.Model)
"""


from .post import slugify, db
from time import time


class Tag(db.Model):
    """
        Class is descendant of db.Model.
        It creates table Tag in db.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)

    def generate_slug(self):
        """
        Function what generate slug from self.title or time()
        :return: None
        """
        if self.title:
            self.slug = slugify(self.title)
            return self.slug
        else:
            self.slug = str(int(time()))
            return self.slug

    def __init__(self, *args, **kwargs):
        """
        Initialisation function
        :return: None
        """
        super().__init__(*args, **kwargs)
        self.slug = self.generate_slug()

    def __repr__(self):
        """
        Function what define the result of a Class
        :return: result
        """
        return f'<Tag id: {self.id}, title: {self.title}>'
