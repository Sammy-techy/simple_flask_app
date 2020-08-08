from sqlalchemy import Column, Integer, String, DateTime
from models.database import db
import datetime


class Posts(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    comment = Column(String(5000))
    created_time = Column(DateTime(), nullable=False)


    def __init__(self, comment, title):
        self.title = title
        self.comment = comment
        self.created_time = datetime.datetime.now()

    def __repr__(self):
        return '<Comment %r>' % (self.id)
