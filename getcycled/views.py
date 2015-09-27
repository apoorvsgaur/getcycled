"""
Routes and views for the flask application.
"""
import os

from flask import Flask
from flask import render_template
from time import time
from flask.ext.sqlalchemy import SQLAlchemy
from getcycled import app, db
from datetime import datetime

from Models import User





@app.route('/')
@app.route('/home')
def home():

    
    return render_template(
        'index.html',
        title='Home',
        year=datetime.now().year
    )

@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/signup', methods=['GET', 'POST'])
def signup():
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