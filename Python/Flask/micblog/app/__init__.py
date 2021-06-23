# -*- coding:utf-8 -*-

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flaskext.markdown import Markdown

from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

Markdown(app)
app.config.from_object('config')

# 初始化数据库
db = SQLAlchemy(app)

# 初始化flask-login
lm = LoginManager()
lm.init_app(app)

def md5(tmp_str):
    import hashlib
    m = hashlib.md5() 
    m.update(tmp_str)
    return m.hexdigest()

from app import views, models
