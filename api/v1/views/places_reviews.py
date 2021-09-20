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
from models.review import Review
from models import storage
from flask import request
from flask import abort


@app_views.route('/places/<place_id>/reviews', strict_slashes=False)
def retrive_reviews(place_id):
    """Retrieves the list of all State objects"""
    try:
        review_list = []
        place_obj = storage.get(Place, place_id)
        for review_obj in place_obj.reviews:
            review_list.append(review_obj.to_dict())
        return (jsonify(review_list))
    except:
        abort(404)


@app_views.route('/reviews/<review_id>', strict_slashes=False)
def retrive_reviews_by_id(review_id):
    """Retrieves a State object"""
    try:
        obj = storage.get(Review, review_id)
        return (jsonify(obj.to_dict()))
    except:
        abort(404)


@app_views.route(
    '/reviews/<review_id>',
    strict_slashes=False,
    methods=['DELETE']
)
def delete_reviews_by_id(review_id):
    """Deletes a State object"""
    try:
        obj = storage.get(Review, review_id)
        State.delete(obj)
        storage.save()
        return ({}), 200
    except:
        abort(404)


@app_views.route(
    'places/<place_id>/reviews',
    strict_slashes=False,
    methods=['POST'])
def create_reviews(place_id):
    """Creates a State"""
    json_data = request.get_json()
    if not (json_data):
        abort(400, 'Not a JSON')
    elif ('name' not in json_data.keys()):
        abort(400, 'Missing name')
    else:
        try:
            state_obj = storage.get(Place, place_id)
            storage.get(User, user_id)
            new_place = Review()
            if ('user_id' in state_obj.keys()):
                setattr(new_place, 'user_id', json_data['user_id'])
            else:
                abort(400, 'Missing user_id')
            if ('text' in state_obj.keys()):
                setattr(new_place, 'text', json_data['text'])
            else:
                abort(400, 'Missing text')
            storage.new(new_place)
            storage.save()
            return (jsonify(new_place.to_dict()), 201)
        except:
            abort(404)


@app_views.route(
                '/reviews/<review_id>',
                strict_slashes=False,
                methods=['PUT']
                )
def update_reviews(review_id):
    """Updates a State object"""
    try:
        json_data = request.get_json()
        if not (json_data):
            abort(400, 'Not a JSON')
        else:
            obj = storage.get(Review, review_id)
            if ('text' in state_obj.keys()):
                setattr(obj, 'text', json_data['text'])
            storage.save()
            return (jsonify(obj.to_dict()), 200)
    except:
        abort(404)
