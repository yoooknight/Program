#-*- coding:utf-8 -*-
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    """
    每一个属性定义过一个字段
    """
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger(), default = ROLE_USER)
    password = db.Column(db.String(10), index = True, unique = True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return True

    def get_id(self):
        return unicode(self.id)

    @classmethod
    def login_check(cls, user_name, passwd):
        print "-==========================="
        print user_name
        user = cls.query.filter(db.or_(User.nickname == user_name, User.email == user_name)).first()        
 
        if not user or passwd!=user.password:
            return None

        return user

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body= db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    title = db.Column(db.String(25))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Post %r>' % (self.body)
