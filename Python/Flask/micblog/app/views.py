#-*- coding:utf-8 -*-
from flask import render_template, flash, redirect, request, session, url_for, g, Markup
from forms import LoginForm, SignUpForm, AboutMeForm, PublishBlogForm
from flask_login import login_user, logout_user, current_user, login_required
import markdown

from models import User, Post, ROLE_USER, ROLE_ADMIN
from app import app, db, lm, md5

import CommonMark

import sys
import datetime
from string import strip

@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@app.route('/index')
def index():
#     users = User.query.all().first()
    users = User.query.filter().all()
    posts = None
    # user = {'nickname': 'YoooKnight'}
    if not users:
        flash('No user post')
    else:
        # posts = users.posts.all()
        posts = []
        for user in users:
            posts.extend((user.posts.all()))

        # 将列表顺序反过来，这样最新的文章就在最上面
        posts.reverse()
        
    return render_template('index.html', title = 'Home', user = user, posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('index')
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.login_check(request.form.get('user_name'), md5(request.form.get('password')))
#        user = User.login_check('user_name')
        # print '=======================jkafdjkljafsd'
        # print user
        if user:
            login_user(user)
            user.last_seen = datetime.datetime.now()        
        
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash('The DB error!')
                return redirect('/login')

            flash('Login requested for Name' + form.user_name.data)
            flash('passwd: ' + str(form.password.data))        
            flash('remember_me: ' + str(form.remember_me.data))
            return redirect(url_for("users", user_id=current_user.id))
        else:
            flash('Login failed, Your name is not exist!')
        # return redirect('/login')
    return render_template('login.html', title = 'Sign In', form = form)

@app.route('/user/<int:user_id>', methods=['POST', 'GET'])
@login_required
def users(user_id):
    form = AboutMeForm()
    user = User.query.filter(User.id == user_id).first()
    if not user:
        flash("The user is not exists.")
        return redirect("/index")
    blogs = user.posts.all()
        # flash('success to login to a user')
        # return redirect("/index")
    # blogs = user.posts.all()
#    return redirect(url_for("index")) 
    return render_template("user.html", form=form, user=user, blogs=blogs)
#    return render_template("index.html", title = 'HOME', user=user)

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    return render_template('profile.html')


@app.route('/post_detail/<int:post_id>', methods=['POST', 'GET'])
def post_detail(post_id):
    reload(sys)   
    sys.setdefaultencoding('utf8')  

    post_detail = Post.query.filter(Post.id == post_id).first()
   
    post_body = post_detail.body.encode('utf8') 

    print "1111111111111111111111111111111"
    print type(post_body)
    print "1111111111111111111111111111111"
    
    return render_template('post.html', post=post_detail, post_body = post_body)

@app.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    user = User()
    if form.validate_on_submit():
        user_name = request.form.get('user_name')
        user_email = request.form.get('user_email')
        password = md5(request.form.get('password', type = str))

        print "###############################"
        print type(password)
        print "###############################"
    
        register_check = User.query.filter(db.or_(User.nickname == user_name, User.email == user_email)).first()
        if register_check:
            flash("error: The user's name or email alerady exists")
            return redirect('/sign-up')
        if len(user_name) and len(user_email):
            user.nickname = user_name
            user.email = user_email
            user.password= password
            user.role = ROLE_USER
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash('The DB error')
                return redirect('/sign-up')
    flash('the user registed success')
    return render_template('sign_up.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/publish/<int:user_id>', methods = ['POST', 'GET'])
@login_required
def publish(user_id):
    form = PublishBlogForm()
    posts = Post()
    if form.validate_on_submit():
        blog_body = request.form.get('body', type = str)
        title = request.form.get('title', type = str)
        if not len(strip(blog_body)):
            flash("The content is necessary")
            return redirect(url_for("publish", user_id = user_id))
        posts.body = blog_body.decode('utf-8')
        posts.timestamp = datetime.datetime.now()
        posts.user_id = user_id
        posts.title = title.decode('utf-8')
        
        try:
            db.session.add(posts)
            db.session.commit()
        except Exception as e:
            print e
            return redirect(url_for("publish", user_id = user_id))
        return redirect(url_for("index"))
    return render_template("publish.html", form=form)


@app.template_filter('neomarkdown')
def neomarkdown(markdown_content):
    parser = CommonMark.Parser()
    renderer = CommonMark.HtmlRenderer()
    ast = parser.parse(markdown_content)
    html = renderer.render(ast)
    # json = CommonMark.dumpJSON(ast)
    # CommonMark.dumpAST(ast) 
    return html
