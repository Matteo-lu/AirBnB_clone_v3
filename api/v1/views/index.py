#!/usr/bin/python3
"""
index rout to generate status route

"""

from api.v1.views import app_views
from flask import Flask


@app_views.route('/status')
def index():
    return (jsonify({"Status": "OK"}))
