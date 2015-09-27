from getcycled import app, db
from getcycled.models import User
from flask.ext.script import Manager, prompt_bool

manager = Manager(app)

@manager.command
def initdb():
	db.create_all()
	db.session.commit()
	print 'Initialized the database'
@manager.command
def dropdp():
	if prompt_bool("WARNING: YOU WILL LOSE ALL YOUR DATA. Do you wish to continue?"):
		db.drop_all()
		print 'Dropped the database'
if __name == '__main__':
	manager.run()