"""
Module contains functions to work with User DB.

Functions:
    register_user_in_db(email, password, firstname, secondname)
    update_user_from_db(email, NewPassword, NewFirstName, NewSecondName)
    delete_user_from_db(user)
"""
from app import user_datastore, db
from flask import flash
from models import User


def register_user_in_db(email, password, firstname, secondname):
    """
    Function creating new user in database
    :param email: email of account
    :param password: password of account
    :param firstname: first name of account
    :param secondname: second name of account
    :return: None
    """
    try:
        user_datastore.create_user(email=email, password=password, firstname=firstname, secondname=secondname, roles=['user'])
        db.session.commit()
    except:
        flash('Cannot be registered')
    return None


def update_user_from_db(email, NewPassword, NewFirstName, NewSecondName):
    """
    Function updating data of user
    :param email: identifier user account in database
    :param NewPassword: new password of account
    :param NewFirstName: new first name of account
    :param NewSecondName: nem second name of account
    :return:
    """
    try:
        user = User.query.filter_by(email=email).first_or_404()
        user.firstname = NewFirstName
        user.password = NewPassword
        user.secondname = NewSecondName
        db.session.commit()
    except:
        flash('Database error!')
    return None


def delete_user_from_db(user):
    """
    Function deleting user from db
    :param user: user account
    :return: None
    """
    try:
        user_datastore.delete_user(user)
        db.session.commit()
    except:
        flash('Database error!')
    return None
