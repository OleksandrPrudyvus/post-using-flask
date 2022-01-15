"""
Module contains classes for DB.

Classes:
    PostForm(Form)
    UserRegister(Form)
Functions:
    post_update_from_db(post)
    post_create_from_db(post)
    post_delete_from_db(post)
    register_user_in_db(email, password, firstname, secondname)
    update_user_from_db(email, NewPassword, NewFirstName, NewSecondName)
    delete_user_from_db(user)
"""
from .service_forms import UserRegister, PostForm
from .service_user import register_user_in_db, update_user_from_db, delete_user_from_db
from .service_post import post_delete_from_db, post_create_from_db, post_update_from_db
