from app import db

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    poster = db.Column(db.String(100))
    description = db.Column(db.Text)
    year = db.Column(db
