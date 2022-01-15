"""
Module containing the main app instance.
"""

from app import app
from views import view_user
from views import posts
app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(view_user, url_prefix='/')
if __name__ == "__main__":
    app.run(port=8000)