"""
Routes and views for the flask application.
"""
import os
from flask import Flask, request
from flask import render_template
from time import time
from flask.ext.sqlalchemy import SQLAlchemy
from getcycled import app, db
from datetime import datetime

from Models import User
from flask_login import login_required
import json


@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title='Home',
        year=datetime.now().year
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            input_username = request.values.get("email")
            input_password = request.values.get("password")
            response = db.session.query(User.name, User.balance, User.date, User.numBottles).filter_by(name = input_username, pin = input_password).first()
            
            if(not response):
                return '{"success":0, "message":"No Account."}'

            return json.dumps({
                "success":1,
                "name":response[0],
                "balance":response[1],
                "date":response[2],
                "numBottles":response[3]
                })

        except ValueError:
                return '{"success":0, "message":"Pin must be digits."}'

        except Exception, e:
            return str(e)

    else:
        return render_template(
            'Login.html',
            title='Login',
            year=datetime.now().year
        )


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            u = User(request.values.get("email"), request.values.get("password"))
            db.session.add(u)
            db.session.commit()
            return "Account created."

        except Exception, e:
            return "Username already exists."

    else:
        return render_template(
            'signup.html',
            title='Signup',
            year=datetime.now().year
        )


@app.route('/about')
def about():
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/deposit')
def deposit():
    
    return render_template(
        'deposit.html',
        title='Deposit',
        year=datetime.now().year
    )