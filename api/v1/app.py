#!/usr/bin/python3
"""
Creates the  Flask app; and register
the blueprint app_views to Flask instance app.
"""

from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

# CORS is enabled and allowed for origins:
CORS(app, resources={r'/api/v1/*': {'origins': '0.0.0.0'}})

app.register_blueprint(app_views)

app.url_map.strict_slashes = False

@app.teardown_appcontext

def teardown_engine(exception):
    """
    Removes the current SQLAlchemy Session 
    object after each request
    """
    storage.close()

# Handles errors
@app.errorhandler(404)

def not_found(error):
    """Return errormessage `Not Found`"""
    response = {'error': 'Not found'}
    return jsonify(response), 404


if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=HOST, port=PORT, threaded=True)
