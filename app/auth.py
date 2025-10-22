# app/auth.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import SignupForm, SigninForm, ChangePasswordForm
from .models import User
from .extensions import db
from flask_login import login_user, logout_user, current_user, login_required

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Signup successful. Please sign in.', 'success')
        return redirect(url_for('auth.signin'))
    return render_template('signup.html', form=form)


@auth_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            # session created server-side due to Flask-Session
            login_user(user)
            flash('Welcome back!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.home'))
        flash('Invalid credentials', 'danger')
    return render_template('signin.html', form=form)


@auth_bp.route('/signout')
@login_required
def signout():
    logout_user()
    flash('Signed out successfully', 'info')
    return redirect(url_for('auth.signin'))


@auth_bp.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.check_password(form.old_password.data):
            current_user.set_password(form.new_password.data)
            db.session.commit()
            flash('Password updated', 'success')
            return redirect(url_for('main.profile'))
        else:
            flash('Old password incorrect', 'danger')
    return render_template('change_password.html', form=form)
