from sqlalchemy import Column, String, Integer
from models.database import db
import uuid


class Friendform(db.Model):
    __tablename__ = 'friendform'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    def __init__(self, first_name, last_name): 
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<add_friend %r>' % (self)
