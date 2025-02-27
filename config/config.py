import os

class Development():
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = os.getenv("DEBUG")
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")
    

class Production():
    SQLALCHEMY_DATABASE_URI = 'postgresql://alibabaa:12345@http://134.209.24.19:5432/alibabaa'
    SECRET_KEY = '11ae8fcaceff9710e238b932e95072a1'
    # SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    # DEBUG = os.getenv("DEBUG")
    # FLASK_APP = os.getenv("FLASK_APP")
    # FLASK_ENV = os.getenv("FLASK_ENV")

    
# #production for paas-api
# conn = psycopg2.connect(user='alibabaa',
#                         password='12345',
#                         host='localhost',
#                         port='5432',
#                         database='alibabaa')

