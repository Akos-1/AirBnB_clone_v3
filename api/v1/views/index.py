#!/usr/bin/python3
"""A route on object that returns a Json string"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """Returns a Json after route"""
    return jsonify({"status": "OK"})
