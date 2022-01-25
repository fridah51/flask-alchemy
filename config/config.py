import os

class Development():
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = os.getenv("DEBUG")
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")
    

class Production():
    SQLALCHEMY_DATABASE_URI='postgres://mviwkkinunrbdu:a3532701c70b2f41ae9d5b64610fc9d379b8c522ffc21caf5bb8a7d777f2b272@ec2-46-137-120-243.eu-west-1.compute.amazonaws.com:5432/d9a7ai301kqtj0'
    SECRET_KEY = 'ggvgvutvt'
    DEBUG = False
# #production
# conn = psycopg2.connect(user='djweilvcuwseru',
#                         password='1ff6d594331d891c1b1296386d289248370ce544f138a77d288c9484715b2f38',
#                         host='ec2-18-203-64-130.eu-west-1.compute.amazonaws.com',
#                         port='5432',
#                         database='d795ll8t69t486')