# app/views.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .forms import EditProfileForm
from .extensions import db

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return redirect(url_for('main.home'))


@main_bp.route('/home')
@login_required
def home():
    return render_template('home.html')


@main_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@main_bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(obj=current_user)
    if form.validate_on_submit():
        # username change not allowed for simplicity
        current_user.full_name = form.full_name.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Profile updated', 'success')
        return redirect(url_for('main.profile'))
    return render_template('edit_profile.html', form=form)
