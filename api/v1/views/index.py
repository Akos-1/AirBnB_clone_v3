#!/usr/bin/python3
"""A route is created for object"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])

def api_status():
    """a JSON response for RESTful API health is returned"""

    response = {'status': 'OK'}
    return jsonify(response)

@app_views.route('/stats', methods=['GET'])

def get_stats():
    """the number of each objects by type is retrieved"""
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)
