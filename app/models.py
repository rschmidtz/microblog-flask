from app import db
from datetime import datetime
from hashlib import md5



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64),index=True,unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(120),index=True,unique=True)
    about_me = db.Column(db.Text(200))
    last_seen = db.Column(db.DateTime)
    posts = db.relationship('Post', backref='author', lazy='dynamic')



    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)


    def __init__(self,nickname,password,email):
        self.nickname = nickname
        self.email = email

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' %self.nickname

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
