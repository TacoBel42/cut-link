from app import *


class Urls_and_token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(4096), unique=True)
    token = db.Column(db.String(12), unique=True)
