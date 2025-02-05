#!/usr/bin/python3
"""
endpoint (route) that will be to return the API status

"""

from api.v1.views import app_views
from flask import Flask
from models import storage
from flask import make_response
from flask import jsonify
from os import getenv
from flask_cors import CORS

if getenv("HBNB_API_HOST") is None:
    HBNB_API_HOST = '0.0.0.0'
else:
    HBNB_API_HOST = getenv("HBNB_API_HOST")
if getenv("HBNB_API_PORT") is None:
    HBNB_API_PORT = '5000'
else:
    HBNB_API_PORT = getenv("HBNB_API_PORT")

app = Flask(__name__)
app.register_blueprint(app_views)
app.strict_slashes = False
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def show_teardown(exception):
    """method to handle teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """handler for 404 errors that returns a JSON-formatted 404 response"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
