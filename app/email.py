from app import mail
from flask_mail import Message
from threading import Thread
from flask import current_app, render_template


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject,template, **kwargs):
    msg = Message(current_app.config['MAIL_SUBJECT_PREFIX'] + subject, \
        sender=current_app.config['ADMIN_EMAIL'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[current_app, msg])
    thr.start()
    return thr

