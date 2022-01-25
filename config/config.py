import os

class Development():
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = os.getenv("DEBUG")
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")
    

class Production():
    SQLALCHEMY_DATABASE_URI='postgresql://tpqyogvupfpiuh:a2eb22348ecb7bcd49217b088d170302e9b0bc82a27ece7d2baea0e16bc1f093@ec2-52-208-185-143.eu-west-1.compute.amazonaws.com:5432/d25bjau5n2s2rb'
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