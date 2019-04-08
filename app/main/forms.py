from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField,SelectField
from wtforms.validators import DataRequired, Email, Regexp, EqualTo, Length
from wtforms import ValidationError
from app.models import User
from flask_pagedown.fields import PageDownField


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')



class RegistrationForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
    username = StringField('Username', validators=[DataRequired(),\
         Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,\
             'username must be only letters') ])
    name = StringField('Full name')
    location = StringField('Your location')
    about_me = StringField('About me')
    password = PasswordField('Password', validators=[DataRequired(), \
        EqualTo('password2', message='passwords must match'),])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def verify_email(self, email_field):
        if User.query.filter_by(email=email_field).first():
            raise ValidationError('Email already registered')

    def verify_username(self, name_field):
        if User.query.filter_by(email=name_field).first():
            raise ValidationError('Username already registered')


class EditProfileForm(Form):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit') 

class EditProfileAdminForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64), \
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,\
            'Usernames must have only letters,numbers, dots or underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and \
            User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.') 


class PostForm(Form):
    body = PageDownField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(Form):
    body = StringField('Enter your comment', validators=[DataRequired()])
    submit = SubmitField('Submit') 
