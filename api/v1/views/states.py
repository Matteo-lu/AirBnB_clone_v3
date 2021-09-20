#!/usr/bin/python3
"""
module to create a new view for State objects that
handles all default RESTFul API actions

"""

from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from models.state import State
from models import storage
from flask import request
from flask import abort


@app_views.route('/states', strict_slashes=False)
def retriveve_states():
    """Retrieves the list of all State objects"""
    obj_list = []
    obj_dict = storage.all(State)
    for value in obj_dict.values():
        obj_list.append(State.to_dict(value))
    return (jsonify(obj_list))


@app_views.route('/states/<state_id>', strict_slashes=False)
def retriveve_states_by_id(state_id):
    """Retrieves a State object"""
    try:
        obj = storage.get(State, state_id)
        return (jsonify(State.to_dict(obj)))
    except:
        abort(404)


@app_views.route(
                '/states/<state_id>',
                strict_slashes=False,
                methods=['DELETE']
                )
def delete_states_by_id(state_id):
    """Deletes a State object"""
    try:
        obj = storage.get(State, state_id)
        State.delete(obj)
        storage.save()  # Check
        return ({}), 200
    except:
        abort(404)


@app_views.route('/states', strict_slashes=False,  methods=['POST'])
def create_states():
    """Creates a State"""
    json_data = request.get_json()
    if not (json_data):
        abort(400, 'Not a JSON')
    elif ('name' not in json_data.keys()):
        abort(400, 'Missing name')
    else:
        new_state = State()
        new_state.name = json_data['name']
        new_state.save()  # Check
        return (jsonify(State.to_dict(new_state)), 201)


@app_views.route('/states/<state_id>', strict_slashes=False,  methods=['PUT'])
def update_states(state_id):
    """Updates a State object"""
    try:
        json_data = request.get_json()
        if not (json_data):
            abort(400, 'Not a JSON')
        elif ('name' not in json_data.keys()):
            abort(400, 'Missing name')
        else:
            obj = storage.get(State, state_id)
            attributes = dir(obj)
            obj.name = json_data['name']  # Check
            obj.save()
            return (jsonify(State.to_dict(obj)))
    except:
        abort(404)
