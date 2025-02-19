from enum import unique

from app import db

class URL(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    short_url = db.Column(db.String, unique=True, nullable=False)