from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return render_template("logout.html")


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be more then 3 characters', category='error')
        if password1 != password2:
            flash('Passwords do not match', category='error')
        if len(password1) < 7:
            flash('Password must be more than 6 characters', category='error')
        else:
            new_user = User(email=email, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash('User created!', category='success')

    return render_template("sign-up.html")
