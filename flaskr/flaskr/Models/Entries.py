from flask_sqlalchemy import SQLAlchemy
from flaskr import app

db = SQLAlchemy(app)


class Entries(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    text = db.Column(db.String)
    def __repr__(self):
        return 'id:%d, title: %s, text: %s ' % (self.id, self.title, self.text)