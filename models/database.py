from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://username:passsword@localhost:3306/dbname"
app.config['SQLALCHEMY_POOL_RECYCLE'] = 2000
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


def init_db():
    print('You are connected to database successfully')

