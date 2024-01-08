#!/usr/bin/python3
'''Contains the users view for the API.'''
from flask import jsonify, request


from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'])
@app_views.route('/users/<user_id>', methods=['GET'])
def get_users(user_id=None):
    '''Gets all users or a specific user using a given userID.
    '''