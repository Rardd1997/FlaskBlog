import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
	
	#sqlalchemy variables
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	#mail variables
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['<your admin account>']
	
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'ru', 'uk']
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    BLOG_NAME = 'My Awesome Blog'
