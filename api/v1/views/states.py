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
def retrive_states():
    """Retrieves the list of all State objects"""
    obj_list = []
    obj_dict = storage.all(State)
    for value in obj_dict.values():
        obj_list.append(State.to_dict(value))
    return (jsonify(obj_list))


@app_views.route('/states/<state_id>', strict_slashes=False)
def retrive_states_by_id(state_id):
    """Retrieves a State object"""
    all_states = storage.all(State)
    for state_obj in all_states.values():
        if state_id == state_obj.id:
            return (jsonify(state_obj.to_dict()))
    abort(404)


@app_views.route(
                '/states/<state_id>',
                strict_slashes=False,
                methods=['DELETE']
                )
def delete_states_by_id(state_id):
    """Deletes a State object"""
    all_states = storage.all(State)
    for state_obj in all_states.values():
        if state_id == state_obj.id:
            state_obj.delete()
            storage.save()
            return ({}), 200
    abort(404)


@app_views.route('/states', strict_slashes=False,  methods=['POST'])
def create_states():
    """Creates a State"""
    if not (request.json):
        abort(400, 'Not a JSON')
    json_data = request.get_json()
    if ('name' not in json_data.keys()):
        abort(400, 'Missing name')
    else:
        new_state = State()
        new_state.name = json_data['name']
        new_state.save()
        return (jsonify(State.to_dict(new_state)), 201)


@app_views.route('/states/<state_id>', strict_slashes=False,  methods=['PUT'])
def update_states(state_id):
    """Updates a State object"""
    all_states = storage.all(State)
    for state_obj in all_states.values():
        if state_id == state_obj.id:
            if not (request.json):
                abort(400, 'Not a JSON')
            json_data = request.get_json()
            for k, v in json_data.items():
                if k in ['update_at', 'create_at', 'id']:
                    continue
                else:
                    setattr(state_obj, k, v)
                    state_obj.save()
                    return (jsonify(State.to_dict(obj)), 200)
        abort(404)
