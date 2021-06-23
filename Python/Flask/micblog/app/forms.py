from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(Form):
    user_name = TextField('user_name', validators = [DataRequired()])
    password= TextField('password', validators = [DataRequired()])
    remember_me= BooleanField('Remember_me',default = False) 
    submit = SubmitField('Log in')

class AboutMeForm(Form):
    describe = TextAreaField('about me', validators = [DataRequired(), Length(max=140)])
    submit = SubmitField('YES!')

class SignUpForm(Form):
    user_name = TextField('user_name', validators=[DataRequired(), Length(max=15)])
    user_email= TextField('user_email', validators=[DataRequired(), Email(), Length(max=15)])
    password = TextField('password', validators=[DataRequired(), Length(max=15)])
    submit = SubmitField('Sign up')

class PublishBlogForm(Form):
    title= TextField('title', validators = [DataRequired()])
    body= TextAreaField('Content', validators = [DataRequired()])
    submit = SubmitField('Submit')
