from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegisterForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email=EmailField('Email', validators=[DataRequired(), Email()])
    password=PasswordField("Password", validators=[DataRequired()])
    confirm_password=PasswordField("Confirm", validators=[DataRequired(), EqualTo('password')])

    submit=SubmitField('Submit')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('This username is taken.')
    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('You are already registered.')    

        

class LoginForm(FlaskForm):
    email=EmailField('Email', validators=[DataRequired(), Email()])
    password=PasswordField("Password", validators=[DataRequired()])
    remember=BooleanField('Remember me')

    submit=SubmitField('Submit')



