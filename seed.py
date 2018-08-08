"""Utility file to seed product data to database"""

from model import Product
from model import connect_to_db, db
from server import app


def load_products():
	"""Load products into database"""

	print "Products"
	product_id = 0
	with open('items.json') as file:
		for title in file:
			title = title.rstrip().strip(',')
			product = Product(product_id=product_id, title=title)
			product_id += 1
			db.session.add(product)
		db.session.commit()

if __name__ == "__main__":
	
	connect_to_db(app)

	db.create_all()

	load_products()

