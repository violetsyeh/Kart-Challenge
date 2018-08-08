"""Model and database function for Kart"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
	"""Products of Kart"""

	__tablename__ = 'products'

	product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	title = db.Column(db.String(64))

	def __repr__(self):
		"""Provides helpful representation when printed"""

		return "<Product product_id={} title={}".format(self.product_id, self.title)


def connect_to_db(app):
	"""Connect the database to Flask app."""

	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///kart'
	app.config['SQALCHMEY_TRACK_MODIFICATIONS'] = False 
	db.app = app
	db.init_app(app)

if __name__ == "__main__":

	from server import app
	connect_to_db(app)
	print "Connected to DB."