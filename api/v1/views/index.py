#!/usr/bin/python3
"""A route on object that returns a Json string"""

from flask import Blueprint
from api.v1.views import app_views
from flask import jsonify

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})
