# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(3, 80)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(6, 128)])
    password2 = PasswordField('Confirm Password', validators=[
                              DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already taken.')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')


class SigninForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class EditProfileForm(FlaskForm):
    full_name = StringField('Full name', validators=[Length(max=255)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    new_password = PasswordField('New password', validators=[
                                 DataRequired(), Length(6, 128)])
    new_password2 = PasswordField('Confirm new', validators=[
                                  DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')
