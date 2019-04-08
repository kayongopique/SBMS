from flask import render_template, session, redirect, url_for, flash, request
from . import auth
from app.main.forms import LoginForm, RegistrationForm
from app.models import User
from app import db
from flask_login import login_user, logout_user, login_required, current_user
from app.email import send_mail
import app


@auth.route('/login', methods=(['GET', 'POST']))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)  
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('invalid username or password')
    return render_template('auth/login.html', form=form)

@auth.route('/register', methods=(['GET', 'POST']))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, name=form.name.data, \
            location=form.location.data, password=form.password.data,\
                  about_me=form.about_me.data)
        db.session.add(user)
        db.session.commit()        
        token = user.generate_token()        
        send_mail(user.email, 'Confirm Your Account', \
            'auth/email/confirm', user=user, token=token)        
        flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('Thanks for confirming your account')
    else:
        flash('The confirmation link has expired')
    return redirect(url_for('main.index'))


@auth.route('/unconfirmed' )
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index')) 
    return render_template('auth/unconfirmed.html') 


@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed and request.endpoint and request.endpoint[:5] != 'auth.' \
            and request.endpoint != 'static':
            return redirect(url_for('auth.unconfirmed'))
    


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_token()        
    send_mail(current_user.email, 'Confirm Your Account', \
        'auth/email/confirm', user=current_user, token=token)        
    flash('A new confirmation mail has been resent to your  email.')
    return redirect(url_for('main.index'))



@auth.route('/logout', methods=(['GET', 'POST']))
@login_required
def logout():
    logout_user()
    flash('you are logged out')
    return redirect(url_for('main.index'))