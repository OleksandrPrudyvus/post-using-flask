"""
Module contains class Config for app config.
"""
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sql/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'gdhvnakARTWo85'
    SECURITY_PASSWORD_SALT = 'asdfdwer1'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True,
    SESSION_COOKIE_SAMESITE = 'Lax'
