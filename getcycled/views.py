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





@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title='Home',
        year=datetime.now().year
    )

@app.route('/login')
def login():
    return render_template(
        'Login.html',
        title='Login',
        year=datetime.now().year
    )


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            return request.data
            u = User('fuckthisshitA', 1223231)
            db.session.add(u)
            db.session.commit()

        except Exception, e:
            return str(e)

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
@login_required
def deposit():

    
    return render_template(
        'deposit.html',
        title='Deposit',
        year=datetime.now().year
    )