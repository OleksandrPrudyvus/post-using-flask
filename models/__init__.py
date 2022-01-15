"""
Module contains classes for DB.

Classes:
    Tag(db.Model)
    Post(db.Model)
    User(db.Model, UserMixin)
    Role(db.Model, RoleMixin)
"""

from .tag import Tag
from .post import Posts
from .user import User, roles_users, Role
