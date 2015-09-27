import os

from flask import Flask
from time import time
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'UserData.db')
db = SQLAlchemy(app)

class User(db.Model):
	name = db.Column(db.String(), primary_key=True)
	pin = db.Column(db.Integer, unique=False)
	balance = db.Column(db.Float, unique=False)
	date = db.Column(db.Float, unique = False)
	numBottles = db.Column(db.Integer, unique = False)
	def __init__(self, name, pin):
		self.name = name
		self.pin = pin
		self.balance = 0
		self.date = int(time())
		self.numBottles = 0
	def __repr__(self):
		return '<User %r>' % self.name 