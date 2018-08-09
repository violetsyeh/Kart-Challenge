from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


db = SQLAlchemy()
# app = Flask(__name__)
# ma = Marshmallow(app)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///kart' + os.path.join(basedir, 'model.postgresql')
# app.config['SQALCHMEY_TRACK_MODIFICATIONS'] = False 


class Product(db.Model):
	"""Products"""

	__tablename__ = 'products'

	product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	title = db.Column(db.String(64))

	def __repr__(self):
		"""Provides helpful representation when printed"""

		return "<Product product_id={} title={}".format(self.product_id, self.title)


# @app.route("/suggestions", methods=["GET"])
# def get_product():
# 	all_products = User.query.all()
# 	print all_products
# 	return jsonify(result.data)

# if __name__ == '__main__':
#     app.run(debug=True)



# class Kart(db.Model):
# 	"""Productss in kart"""

# 	__tablename__ = 'karts'
	



def connect_to_db(app):
	"""Connect the database to Flask app."""

	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///kart'
	# app.config['SQALCHMEY_TRACK_MODIFICATIONS'] = False 
	db.app = app
	db.init_app(app)

if __name__ == "__main__":

	from server import app
	connect_to_db(app)
	# app.run(debug=True)
	# app.run(port=5000, host='0.0.0.0')
	print "Connected to DB."