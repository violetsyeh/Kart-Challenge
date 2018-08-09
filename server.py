from flask_debugtoolbar import DebugToolbarExtension

from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify)

from model import Product, connect_to_db, db

import requests

app = Flask(__name__)


app.secret_key = "ABC"

@app.route('/')
def index():
	"""Homepage."""

	return render_template("index.html")

@app.route('/add-to-kart', methods=['GET'])
def add_to_kart():
    """Get item to add to kart"""
    
    item = request.args.get("item")
    
    return item





if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode


    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True

    app.run(port=5000, host='0.0.0.0')