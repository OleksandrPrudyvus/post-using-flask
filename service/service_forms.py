"""
Module contains class Form, for use form  on the site

Classes:
    PostForm(Form)
    UserRegister(Form)
"""
from wtforms import Form, StringField, TextAreaField, PasswordField


class PostForm(Form):
    """
    Class is descendant of Form , from wtforms.
    Class create fields:
		title: StringField('Title')
		body: TextAreaField('Body')
		tag: StringField('Tag')
    """
    title = StringField('Title')
    body = TextAreaField('Body')
    tag = StringField('Tag')


class UserRegister(Form):
    """
        Class is descendant of Form , from wtforms.
        Class create fields:
			firstname: StringField('FirstName')
			secondname: StringField('SecondName')
			email: StringField("Email")
			password: PasswordField('Password')
			password_repeat: PasswordField('Password repeat')
    """
    firstname = StringField('FirstName')
    secondname = StringField('SecondName')
    email = StringField("Email")
    password = PasswordField('Password')
    password_repeat = PasswordField('Password repeat')
