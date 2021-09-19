#!/usr/bin/python3
"""
endpoint (route) that will be to return the API status

"""

from api.v1.views import app_views
from flask import Flask
from models import storage
from flask import make_response
from flask import jsonify

app = Flask(__name__)
app.register_blueprint(app_views)
app.strict_slashes = False


@app.teardown_appcontext
def show_teardown(exception):
    """method to handle teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """handler for 404 errors that returns a JSON-formatted 404 response"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", threaded=True)
