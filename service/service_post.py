"""
Module contains functions to work with Posts DB.

Functions:
    post_update_from_db(post)
    post_create_from_db(post)
    post_delete_from_db(post)
"""

from .service_forms import PostForm
from app import db
from flask import request, flash


def post_update_from_db(post):
    """
    Function updating 'post' from db
    :param post: object of the 'Posts' class what need updating
    :return:None
    """
    try:
        form = PostForm(request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()
    except:
        return flash("Database error")
    return None


def post_create_from_db(post):
    """
    Function creating object 'post' in database
    :param post: object of the Posts class
    :return: None
    """
    try:
        db.session.add(post)
        db.session.commit()
    except:
        return flash('Database error')
    return None


def post_delete_from_db(post):
    """
    Function deleting object 'post' from db
    :param post: object of the Posts class
    :return: None
    """
    try:
        db.session.delete(post)
        db.session.commit()
    except:
        return flash('Database error!')
    return None

