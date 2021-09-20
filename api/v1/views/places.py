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
from models.place import Place
from models.user import User
from models import storage
from flask import request
from flask import abort


@app_views.route('/cities/<city_id>/places', strict_slashes=False)
def retrive_places(city_id):
    """Retrieves the list of all State objects"""
    try:
        places_list = []
        city_obj = storage.get(City, city_id)
        for place_obj in city_obj.places:
            places_list.append(place_obj.to_dict())
        return (jsonify(places_list))
    except:
        abort(404)


@app_views.route('/places/<place_id>', strict_slashes=False)
def retrive_places_by_id(place_id):
    """Retrieves a State object"""
    try:
        obj = storage.get(Place, place_id)
        return (jsonify(obj.to_dict()))
    except:
        abort(404)


@app_views.route(
    '/places/<place_id>',
    strict_slashes=False,
    methods=['DELETE']
)
def delete_place_by_id(place_id):
    """Deletes a State object"""
    try:
        obj = storage.get(Place, place_id)
        State.delete(obj)
        storage.save()
        return ({}), 200
    except:
        abort(404)


@app_views.route(
    '/cities/<city_id>/places',
    strict_slashes=False,
    methods=['POST'])
def create_place(city_id):
    """Creates a State"""
    json_data = request.get_json()
    if not (json_data):
        abort(400, 'Not a JSON')
    elif ('name' not in json_data.keys()):
        abort(400, 'Missing name')
    else:
        try:
            state_obj = storage.get(City, city_id)
            storage.get(User, user_id)
            new_place = Place()
            if ('user_id' in state_obj.keys()):
                setattr(new_place, 'user_id', json_data['user_id'])
            else:
                abort(400, 'Missing user_id')
            if ('name' in state_obj.keys()):
                setattr(new_place, 'name', json_data['name'])
            else:
                abort(400, 'Missing name')
            storage.new(new_place)
            storage.save()
            return (jsonify(new_place.to_dict()), 201)
        except:
            abort(404)


@app_views.route('/places/<place_id>', strict_slashes=False,  methods=['PUT'])
def update_place(place_id):
    """Updates a State object"""
    try:
        json_data = request.get_json()
        if not (json_data):
            abort(400, 'Not a JSON')
        elif ('name' not in json_data.keys()):
            abort(400, 'Missing name')
        else:
            obj = storage.get(Place, place_id)
            if ('name' in state_obj.keys()):
                setattr(obj, 'name', json_data['name'])
            if ('description' in state_obj.keys()):
                setattr(obj, 'description', json_data['description'])
            if ('number_rooms' in state_obj.keys()):
                setattr(obj, 'number_rooms', json_data['number_rooms'])
            if ('number_bathrooms' in state_obj.keys()):
                setattr(obj, 'number_bathrooms', json_data['number_bathrooms'])
            if ('max_guest' in state_obj.keys()):
                setattr(obj, 'max_guest', json_data['max_guest'])
            if ('price_by_night' in state_obj.keys()):
                setattr(obj, 'price_by_night', json_data['price_by_night'])
            if ('latitude' in state_obj.keys()):
                setattr(obj, 'latitude', json_data['latitude'])
            if ('longitude' in state_obj.keys()):
                setattr(obj, 'longitude', json_data['longitude'])
            storage.save()
            return (jsonify(obj.to_dict()), 200)
    except:
        abort(404)
