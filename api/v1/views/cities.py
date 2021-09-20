#!/usr/bin/python3
"""
module to create a new view for State objects that
handles all default RESTFul API actions

"""

from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from models.city import City
from models.state import State
from models import storage
from flask import request
from flask import abort


@app_views.route('/states/<state_id>/cities', strict_slashes=False)
def retrive_cities(state_id):
    """Retrieves the list of all State objects"""
    try:
        city_list = []
        state_obj = storage.get(State, state_id)
        for city_obj in state_obj.cities:
            city_list.append(city_obj.to_dict())
        return (jsonify(city_list))
    except:
        abort(404)


@app_views.route('/cities/<city_id>', strict_slashes=False)
def retrive_cities_by_id(city_id):
    """Retrieves a State object"""
    try:
        obj = storage.get(City, city_id)
        return (jsonify(obj.to_dict()))
    except:
        abort(404)


@app_views.route(
                '/cities/<city_id>',
                strict_slashes=False,
                methods=['DELETE']
                )
def delete_city_by_id(city_id):
    """Deletes a State object"""
    try:
        obj = storage.get(City, city_id)
        State.delete(obj)
        storage.save()
        return ({}), 200
    except:
        abort(404)


@app_views.route(
                '/states/<state_id>/cities',
                strict_slashes=False,
                methods=['POST'])
def create_city(state_id):
    """Creates a State"""
    json_data = request.get_json()
    if not (json_data):
        abort(400, 'Not a JSON')
    elif ('name' not in json_data.keys()):
        abort(400, 'Missing name')
    else:
        try:
            state_obj = storage.get(State, state_id)
            new_city = City()
            setattr(new_city, 'name', json_data['name'])
            setattr(new_city, 'state_id', state_id)
            storage.new(new_city)
            storage.save()
            return (jsonify(new_city.to_dict()), 201)
        except:
            abort(404)


@app_views.route('/cities/<city_id>', strict_slashes=False,  methods=['PUT'])
def update_city(city_id):
    """Updates a State object"""
    try:
        json_data = request.get_json()
        if not (json_data):
            abort(400, 'Not a JSON')
        elif ('name' not in json_data.keys()):
            abort(400, 'Missing name')
        else:
            obj = storage.get(City, city_id)
            setattr(obj, 'name', json_data['name'])
            storage.save()
            return (jsonify(obj.to_dict()), 200)
    except:
        abort(404)
