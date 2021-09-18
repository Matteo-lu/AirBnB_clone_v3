#!/usr/bin/python3
"""
endpoint (route) that will be to return the API status

"""

from api.v1.views import app_views
from flask import Flask
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)
app.strict_slashes = False


@app.route('/')
def home():
    return jsonify({"Hello": "World"})


@app.teardown_appcontext
def show_teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", threaded=True)
