import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('SECRET_KEY') or 'itsasecret'
# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://addressadmin:addressadmin@localhost/adressbook'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASEDIR, 'address_book.db')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') or True
NOTIFICATION_EMAIL = os.environ.get('NOTIFICATION_EMAIL') or 'your@email.com'
