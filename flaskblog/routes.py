from flaskblog import app, db, bcrypt
from flask import render_template, url_for, redirect, flash
from flaskblog.forms import RegisterForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user

posts = [
    {'title': 'How to become rich in less than an hour',
     'date_posted': 'Feb 17, 2026',
     'content': 'There are tons of people who want to become rich without any stress or work.',
     'author': 'Mingliboyev Jahongir'},
    {'title': 'How to become rich in less than an hour',
     'date_posted': 'Feb 17, 2026',
     'content': 'There are tons of people who want to become rich without any stress or work.',
     'author': 'Mingliboyev Jahongir'}
]

@app.route('/')
def home():
    return render_template('main.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account was created! Now you can log in.", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
    


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('You successfully logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash("We could NOT log you in! Please check email or password", 'danger')
    return render_template('login.html', form=form)