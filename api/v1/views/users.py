#!/usr/bin/python3
"""
module to create a new view for State objects that
handles all default RESTFul API actions

"""

from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from models.user import User
from models import storage
from flask import request
from flask import abort


@app_views.route('/users', strict_slashes=False)
def retrive_users():
    """Retrieves the list of all State objects"""
    obj_list = []
    obj_dict = storage.all(User)
    for value in obj_dict.values():
        obj_list.append(value.to_dict())
    return (jsonify(obj_list))


@app_views.route('/users/<user_id>', strict_slashes=False)
def retrive_user_by_id(user_id):
    """Retrieves a State object"""
    try:
        obj = storage.get(User, user_id)
        return (jsonify(obj.to_dict()))
    except:
        abort(404)


@app_views.route(
    '/users/<user_id>',
    strict_slashes=False,
    methods=['DELETE']
)
def delete_user_by_id(user_id):
    """Deletes a State object"""
    try:
        obj = storage.get(User, user_id)
        State.delete(obj)
        storage.save()
        return ({}), 200
    except:
        abort(404)


@app_views.route('/users', strict_slashes=False,  methods=['POST'])
def create_user():
    """Creates a State"""
    json_data = request.get_json()
    if not (json_data):
        abort(400, 'Not a JSON')
    elif ('name' not in json_data.keys()):
        abort(400, 'Missing name')
    else:
        new_user = User()
        if ('password' in json_data.keys()):
            setattr(obj, 'password', json_data['password'])
        else:
            abort(400, 'Missing password')
        if ('email' in json_data.keys()):
            setattr(obj, 'email', json_data['email'])
        else:
            abort(400, 'Missing email')
        if ('first_name' in json_data.keys()):
            setattr(obj, 'first_name', json_data['first_name'])
        elif ('last_name' in json_data.keys()):
            setattr(obj, 'last_name', json_data['last_name'])

        storage.new(new_user)
        storage.save()
        return (jsonify(State.to_dict(new_user)), 201)


@app_views.route(
                '/users/<user_id>',
                strict_slashes=False,
                methods=['PUT']
                )
def update_user(user_id):
    """Updates a State object"""
    try:
        json_data = request.get_json()
        if not (json_data):
            abort(400, 'Not a JSON')
        else:
            obj = storage.get(User, user_id)
            if ('first_name' in json_data.keys()):
                setattr(obj, 'first_name', json_data['first_name'])
            elif ('last_name' in json_data.keys()):
                setattr(obj, 'last_name', json_data['last_name'])
            elif ('password' in json_data.keys()):
                setattr(obj, 'password', json_data['password'])
            storage.save()
            return (jsonify(obj.to_dict()), 200)
    except:
        abort(404)
