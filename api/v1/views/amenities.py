#!/usr/bin/python3
"""
module to create a new view for State objects that
handles all default RESTFul API actions

"""

from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from models.state import State
from models.amenity import Amenity
from models import storage
from flask import request
from flask import abort


@app_views.route('/amenities', strict_slashes=False)
def retrive_amenities():
    """Retrieves the list of all State objects"""
    obj_list = []
    obj_dict = storage.all(Amenity)
    for value in obj_dict.values():
        obj_list.append(value.to_dict())
    return (jsonify(obj_list))


@app_views.route('/amenities/<amenity_id>', strict_slashes=False)
def retrive_amenity_by_id(amenity_id):
    """Retrieves a State object"""
    try:
        obj = storage.get(Amenity, amenity_id)
        return (jsonify(obj.to_dict()))
    except:
        abort(404)


@app_views.route(
    '/amenities/<amenity_id>',
    strict_slashes=False,
    methods=['DELETE']
)
def delete_amenity_by_id(amenity_id):
    """Deletes a State object"""
    try:
        obj = storage.get(Amenity, amenity_id)
        State.delete(obj)
        storage.save()
        return ({}), 200
    except:
        abort(404)


@app_views.route('/amenities', strict_slashes=False,  methods=['POST'])
def create_states():
    """Creates a State"""
    json_data = request.get_json()
    if not (json_data):
        abort(400, 'Not a JSON')
    elif ('name' not in json_data.keys()):
        abort(400, 'Missing name')
    else:
        new_amenity = Amenity()
        new_amenity.name = json_data['name']
        storage.new(new_amenity)
        storage.save()
        return (jsonify(State.to_dict(new_amenity)), 201)


@app_views.route(
                '/amenities/<amenity_id>',
                strict_slashes=False,
                methods=['PUT']
                )
def update_states(amenity_id):
    """Updates a State object"""
    try:
        json_data = request.get_json()
        if not (json_data):
            abort(400, 'Not a JSON')
        elif ('name' not in json_data.keys()):
            abort(400, 'Missing name')
        else:
            obj = storage.get(Amenity, amenity_id)
            setattr(obj, 'name', json_data['name'])
            storage.save()
            return (jsonify(obj.to_dict()), 200)
    except:
        abort(404)
