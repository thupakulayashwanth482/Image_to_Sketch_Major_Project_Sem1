from db import db


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(20), nullable=False, default="default.jpg")
    # name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)