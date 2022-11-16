from platform import machine
from urllib import request
from flask import Blueprint, flash, redirect, render_template, url_for, request
from flask_login import login_required
from flask_mail import Mail, Message
from . import database
import smtplib

# Make invisible
api = Blueprint("api", __name__, url_prefix="/")

email_address = 'parts.service@cesforklift.co.za'
email_password = 'TKPF7WCCTWO8'

api.route("/email", methods=["POST", "GET"])
def email():
    
    with smtplib.SMTP('mail.cesforklift.co.za') as server:
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login(email_address, email_password)

            subject = 'Sales'
            body = f'{name} {surname} {company} {number} {email} {machine}'
            msg = f'Subject: {subject}\n\n{body}'

            server.sendmail(email_address, email_address, msg)
