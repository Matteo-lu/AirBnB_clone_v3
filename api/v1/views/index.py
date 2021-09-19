#!/usr/bin/python3
"""
index rout to generate status route

"""

from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status/', strict_slashes=False)
def index():
    """method to return status ok"""
    return (jsonify(Status="OK"))


@app_views.route('/stats/', strict_slashes=False)
def count_types():
    """method that retrieves the number of each objects by type"""
    classes = {"Amenity": Amenity, "City": City,
               "Place": Place, "Review": Review, "State": State, "User": User}
    my_dict = {}
    for key in classes.keys():
        if (classes[key] == Amenity):
            my_dict["amenities"] = storage.count(classes[key])
        elif (classes[key] == City):
            my_dict["cities"] = storage.count(classes[key])
        elif (classes[key] == Place):
            my_dict["places"] = storage.count(classes[key])
        elif (classes[key] == Review):
            my_dict["reviews"] = storage.count(classes[key])
        elif (classes[key] == State):
            my_dict["states"] = storage.count(classes[key])
        elif (classes[key] == User):
            my_dict["users"] = storage.count(classes[key])
    return (jsonify(my_dict))
