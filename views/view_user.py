"""
Module contains all functions working on post page.

Functions:
    page_not_found()
    register():
    logout()
    account_user()
    account_editing()
    delete_post(slug)
    user_delete()
"""
from flask import render_template, request, flash, redirect, url_for, Blueprint
from models import User
from app import app
from flask_login import logout_user, login_required, current_user
from service.service_forms import UserRegister
from service.service_user import register_user_in_db, delete_user_from_db, update_user_from_db

view_user = Blueprint('view_user', __name__)


@view_user.route('/')
def index():
    """
    Function showing home page
    :return: template home page
    """
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    """
    Function responds to error 404
    :return: template of custom page
    """
    return render_template("includes/404.html"), 404


@view_user.route('/register', methods=["GET", "POST"])
def register():
    """
    Function working on register page:
        1) adding new user in database if method "POST".
        2) showing the fields for registration
    :return: the template of the user register or login page
    """
    form = UserRegister()
    if request.method == "POST":
        firstname = request.form.get('firstname')
        secondname = request.form.get('secondname')
        email = request.form.get('email')
        password = request.form.get('password')
        password_repeat = request.form.get('password_repeat')
        if email == '' or password == '' or password_repeat == '' or firstname == '' or secondname == '':
            flash('Pleas, fill all fields!')
        elif password != password_repeat or User.query.filter_by(email=email).first():
            flash("Email is already registered or passwords do not match!")
        else:
            register_user_in_db(email=email, password=password, firstname=firstname, secondname=secondname)
            return redirect(url_for('security.login')), flash('Successful registration!!!')
    return render_template('user/register.html', form=form)


@view_user.route("/logout_id")
@login_required
def logout():
    """
    Function logging user out
    :return: redirect  to the main page
    """
    logout_user()
    return redirect(url_for('view_user.index')), flash('Logout is successful!!!')


@view_user.route('/account')
@login_required
def account_user():
    """
    Function showing all parameter of user
    :return: template of the user account
    """
    user = current_user
    return render_template('user/user_account.html', user=user)


@view_user.route('/editing_account', methods=['POST', 'GET'])
@login_required
def account_editing():
    """
    Function editing information about  user account
        1) adding change to user account if method 'POST'
        2) showing the fields for change parameters
    :return: template of the user_update or redirect to account_user
    """
    form = UserRegister()
    user = current_user
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        secondname = request.form.get('secondname')
        password = request.form.get('password')
        password_repeat = request.form.get('password_repeat')
        if password == '' or password_repeat == '' or firstname == '' or secondname == '':
            flash('Pleas, fill all fields!')
        elif password != password_repeat:
            flash("Passwords do not match!")
        else:
            update_user_from_db(email=user.email, NewPassword=password,
                                NewFirstName=firstname, NewSecondName=secondname)
            return redirect(url_for('view_user.account_user')), flash('Successful update!!!')
    return render_template('user/user_update.html', user=user, form=form)


@view_user.route('/delete', methods=['GET', 'POST'])
@login_required
def user_delete():
    """
    Function that removes the user
    :return: redirect to index page
    """
    user = current_user
    delete_user_from_db(user)
    return redirect(url_for('view_user.index')), flash('Deleting successful!')
