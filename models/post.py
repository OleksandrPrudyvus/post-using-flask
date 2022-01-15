"""
Module contains class Posts for DB.

Classes:
    Posts(db.Model)
Function:
    slugify(s: str)

"""
from datetime import datetime
from time import time
from app import db
from re import sub


"""
Creating a new table 'posts_tags'. 
with parameters:
    post_id: posts.id
    tag_id: tag.id
"""
posts_tags = db.Table('posts_tags',
                      db.Column('post_id',
                                db.Integer,
                                db.ForeignKey('posts.id')),
                      db.Column('tag_id',
                                db.Integer,
                                db.ForeignKey('tag.id'))
                      )


def slugify(s: str):
    """
    Function creates slug
    :param s: values for conversion
    :return:
    """
    return sub(r'[^\w+]', '-', s)


class Posts(db.Model):
    """
    Class is descendant of db.Model.
    It creates table Posts in db.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())
    tags = db.relationship('Tag', secondary=posts_tags, backref=db.backref('posts'), lazy='dynamic')

    def __init__(self, *args, **kwargs):
        """
        Initialisation function
        :return: None
        """
        super().__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        """
        Function what generate slug from self.title or time()
        :return: None
        """
        if self.title:
            self.slug = slugify(self.title)
        else:
            self.slug = str(int(time()))

    def __repr__(self):
        """
        Function what define the result of a Class
        :return: result
        """
        return f"<Post id: {self.id}, title: {self.title}>"
