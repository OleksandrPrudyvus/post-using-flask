"""
Module contains class User, Role and roles_users for DB.

Classes:
    User(db.Model, UserMixin)
    Role(db.Model, RoleMixin)
"""


from datetime import datetime
from app import db
from flask_security import UserMixin, RoleMixin

"""
Creating a new table 'roles_users'. 
with parameters:
    user_id: user.id
    role_id: role.id
"""
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer,
                                 db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer,
                                 db.ForeignKey('role.id'))

                       )


class User(db.Model, UserMixin):
    """
        Class is descendant of db.Model and UserMixin.
        It creates table User in db.
    """
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    secondname = db.Column(db.String(100))
    created = db.Column(db.DateTime, default=datetime.now())
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users'), lazy='dynamic')


class Role(db.Model, RoleMixin):
    """
        Class is descendant of db.Model and RoleMixin.
        It creates table Role in db.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
