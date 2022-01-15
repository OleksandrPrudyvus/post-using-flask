"""
Module containing factory for app merging it with database, migrate, admin_panel and blueprints.

Classes:
    AdminMixin,
    AdminView(AdminMixin, ModelView),
    BaseModelView(ModelView),
    HomeAdminView(AdminMixin, AdminIndexView),
    PostAdminView(AdminMixin, BaseModelView),
    TagAdminView(AdminMixin, BaseModelView)
"""

from flask import Flask, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security, current_user


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
from models import *
migrate = Migrate(app, db)


class AdminMixin:
    """
    Parent class to customize and protect the admin panel.
    Function:
        is_accessible(self)
        inaccessible_callback(self, name, **kwargs)
    """
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class AdminView(AdminMixin, ModelView):
    """
    Class is descendant of ModelView and AdminMixin.
    """
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    """
    Class is descendant of  AdminMixin and AdminIndexView.
    """
    pass


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        """
        :param form: Form used to create/update model
        :param model: Model that will be created/updated
        :param is_created: Will be set to True if model was created and to False if edited
        :return: super().on_model_change(form, model, is_created)
        """
        if is_created:
            model.generate_slug()
        return super().on_model_change(form, model, is_created)


class PostAdminView(AdminMixin, BaseModelView):
    """
    Class is descendant of  AdminMixin and BaseModelView.

    """
    form_columns = ['title', 'body', 'tags']


class TagAdminView(AdminMixin, BaseModelView):
    """
    Class is descendant of  AdminMixin and BaseModelView.
    """
    form_columns = ['title', 'posts']
class UserAdminView(AdminMixin, BaseModelView):
    """
        Class is descendant of  AdminMixin and BaseModelView.
        """
    form_columns = ['firstname', 'secondname', 'email', 'password']

# admin panel initialization
admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Main'))
# add new views
admin.add_view(PostAdminView(Posts, db.session, endpoint="posted"))
admin.add_view(TagAdminView(Tag, db.session))
admin.add_view(UserAdminView(User, db.session))
admin.add_view(ModelView(Role, db.session))

# create SQLAlchemyUserDatastore object
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
