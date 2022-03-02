import os

class Development():
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = os.getenv("DEBUG")
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")
    

class Production():
    SQLALCHEMY_DATABASE_URI='postgresql://fdxcpgprlhsbwn:1eb19ae264d628d19e9bf2c9ffb7aeffb4e96d76a16810eaaa7309823bef4040@ec2-54-73-178-126.eu-west-1.compute.amazonaws.com:5432/d5bpd849bd40qp'
    SECRET_KEY = '11ae8fcaceff9710e238b932e95072a1'
    # SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    # DEBUG = os.getenv("DEBUG")
    # FLASK_APP = os.getenv("FLASK_APP")
    # FLASK_ENV = os.getenv("FLASK_ENV")
  
    
# #production
# conn = psycopg2.connect(user='',
#                         password='',
#                         host='',
#                         port='5432',
#                         database='')
#SQLALCHEMY_DATABASE_URI = postgresql://postgres:21post@localhost:5432/alchemy
