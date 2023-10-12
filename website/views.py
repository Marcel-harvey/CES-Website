from urllib import request
from flask import Blueprint, redirect, render_template, url_for, request
import smtplib
from dotenv import load_dotenv
import os
from email.message import EmailMessage
import ssl
import smtplib


views = Blueprint("views", __name__, url_prefix="/")

load_dotenv()

EMAIL_SENDER = os.getenv("MAIL_USERNAME")
EMAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
EMAIL_SALES = os.getenv("MAIL_SALES")
EMAIL_OTHER = os.getenv("MAIL_OTHER")

em = EmailMessage()


# Functions that create the visual representation of each page
@views.route("/")
def home_page():

    return render_template("index.html")


@views.route("/Team")
def team():

    return render_template("team.html")


@views.route("/Sales", methods=["GET", "POST"])
def sales():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        company = request.form.get("company")
        number = request.form.get("number")
        email = request.form.get("email")
        machine = request.form.get("size")

        if not name:
            return render_template('Sales.html', error='error', name='name')

        elif not surname:
            return render_template('Sales.html', error='error', name='name')

        elif not company:
            return render_template('Sales.html', error='error', name='name')

        elif not number:
            return render_template('Sales.html', error='error', name='name')

        elif not number:
            return render_template('Sales.html', error='error', name='name')

        elif not email:
            return render_template('Sales.html', error='error', name='name')

        elif not machine:
            return render_template('Sales.html', error='error', name='name')

        else:
            subject = 'Sales'
            body = f'''
Name: {name}
Surname: {surname}
Company: {company}
Number: {number}
Email: {email}
Machine: {machine}

Generated by CES Website
                '''
            message = f"""\
Subject: Parts

{body}"""
            context = ssl.create_default_context()
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.sendmail(EMAIL_SENDER, EMAIL_SALES, message)

            return redirect(url_for("views.sent", email='emailSent', page='Sales'))
    return render_template("sales.html")


@views.route("/Service", methods=["GET", "POST"])
def service():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        company = request.form.get("company")
        number = request.form.get("number")
        email = request.form.get("email")
        model = request.form.get("model")
        serial = request.form.get("serial")
        hours = request.form.get("hours")

        if not name:
            return render_template('Service.html', error='error', name='name')

        elif not surname:
            return render_template('Service.html', error='error')

        elif not company:
            return render_template('Service.html', error='error')

        elif not number:
            return render_template('Service.html', error='error')

        elif not email:
            return render_template('Service.html', error='error')

        elif not model:
            return render_template('Service.html', error='error')

        elif not serial:
            return render_template('Service.html', error='error')

        elif not hours:
            return render_template('Service.html', error='error')

        else:
            subject = 'Service'
            body = f'''
Name: {name}
Surname: {surname}
Company: {company}
Number: {number}
Email: {email}
Model: {model}
Serial: {serial}
Hours: {hours}

Generated by CES Website
                '''

            message = f"""\
Subject: Service

{body}"""
            context = ssl.create_default_context()
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.sendmail(EMAIL_SENDER, EMAIL_OTHER, message)

            return redirect(url_for("views.sent", email='emailSent', page='Service'))
    return render_template("service.html")


@views.route("/Parts", methods=["GET", "POST"])
def parts():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        company = request.form.get("company")
        number = request.form.get("number")
        email = request.form.get("email")
        serial = request.form.get("serial")
        parts = request.form.get("parts")

        if not name:
            return render_template('Parts.html', error='error', name='name')

        elif not surname:
            return render_template('Parts.html', error='error')

        elif not company:
            return render_template('Parts.html', error='error')

        elif not number:
            return render_template('Parts.html', error='error')

        elif not email:
            return render_template('Parts.html', error='error')

        elif not serial:
            return render_template('Parts.html', error='error')

        elif not parts:
            return render_template('Parts.html', error='error')

        else:
            subject = 'Parts'
            body = f'''
Name: {name}
Surname: {surname}
Company: {company}
Number: {number}
Email: {email}
Serial: {serial}
Parts: {parts}

Generated by CES Website
                '''

            message = f"""\
Subject: Parts

{body}"""
            context = ssl.create_default_context()
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.sendmail(EMAIL_SENDER, EMAIL_OTHER, message)

            return redirect(url_for("views.sent", email='emailSent', page='Service'))
    return render_template("parts.html", methods=["GET", "POST"])


@views.route("/Manager", methods=["GET", "POST"])
def manager():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        company = request.form.get("company")
        number = request.form.get("number")
        email = request.form.get("email")
        complaint = request.form.get("manager")

        if not name:
            return render_template('Manager.html', error='error', name='name')

        elif not surname:
            return render_template('Manager.html', error='error')

        elif not company:
            return render_template('Manager.html', error='error')

        elif not number:
            return render_template('Manager.html', error='error')

        elif not email:
            return render_template('Manager.html', error='error')

        elif not complaint:
            return render_template('Manager.html', error='error')

        else:
            subject = 'Manager'
            body = f'''
Name: {name}
Surname: {surname}
Company: {company}
Number: {number}
Email: {email}
Complaint:
{complaint}

Generated by CES Website
                '''
            message = f"""\
Subject: Manager

{body}"""
            context = ssl.create_default_context()
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.sendmail(EMAIL_SENDER, EMAIL_SALES, message)

            return redirect(url_for("views.sent", email='emailSent', page='Service'))
    return render_template("manager.html", methods=["GET", "POST"])


@views.route("/Office", methods=["GET", "POST"])
def office():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        company = request.form.get("company")
        number = request.form.get("number")
        email = request.form.get("email")
        office = request.form.get("office")

        if not name:
            return render_template('Office.html', error='error', name='name')

        elif not surname:
            return render_template('Office.html', error='error', name='name')

        elif not company:
            return render_template('Office.html', error='error', name='name')

        elif not number:
            return render_template('Office.html', error='error', name='name')

        elif not email:
            return render_template('Office.html', error='error', name='name')

        elif not office:
            return render_template('Office.html', error='error', name='name')

        else:
            subject = 'Office'
            body = f'''
Name: {name}
Surname: {surname}
Company: {company}
Number: {number}
Email: {email}
Office:
{office}

Generated by CES Website
                '''
            message = f"""\
Subject: Office

{body}"""
            context = ssl.create_default_context()
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.sendmail(EMAIL_SENDER, EMAIL_OTHER, message)

            return redirect(url_for("views.sent", email='emailSent', page='Service'))
    return render_template("office.html")


@views.route("/Repairs", methods=["GET", "POST"])
def repairs():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        company = request.form.get("company")
        number = request.form.get("number")
        email = request.form.get("email")
        serial = request.form.get("serial")
        problem = request.form.get("problem")

        if not name:
            return render_template('Repairs.html', error='error', name='name')

        elif not surname:
            return render_template('Repairs.html', error='error')

        elif not company:
            return render_template('Repairs.html', error='error')

        elif not number:
            return render_template('Repairs.html', error='error')

        elif not email:
            return render_template('Repairs.html', error='error')

        elif not serial:
            return render_template('Repairs.html', error='error')

        elif not problem:
            return render_template('Repairs.html', error='error')

        else:
            subject = 'Repairs'
            body = f'''
Name: {name}
Surname: {surname}
Company: {company}
Number: {number}
Email: {email}
Serial: {serial}
Problem: {problem}

Generated by CES Website
                '''
            message = f"""\
Subject: Repairs

{body}"""
            context = ssl.create_default_context()
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.sendmail(EMAIL_SENDER, EMAIL_OTHER, message)

            return redirect(url_for("views.sent", email='emailSent', page='Service'))
    return render_template("repairs.html")


@views.route("/sent/<email>/<page>", methods=['GET', 'POST'])
def sent(email, page):
    if email =='emailSent':
        return render_template("sent.html")

    else:
        return redirect(url_for(f'views.{page}'))
    

@views.route("/machine-model", methods=['GET', 'POST'])
def models():

    return render_template("models.html")


@views.route("/machine-specs/<machine>", methods=['GET', 'POST'])
def specs(machine):

    return render_template("specs.html", machine=machine)

