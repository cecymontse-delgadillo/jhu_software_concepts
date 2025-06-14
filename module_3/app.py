"""
app.py - Application Factory for Grand Cafe Analysis
-------------------------------------------------
This script initializes and runs a Flask web application.
Features:
- Uses the Flask application factory pattern via create_app()
- Registers a blueprint named 'pages' which contains route definitions
- Can be run directly with `python app.py` for local development

Usage:
    $ flask run          # via Flask CLI
    OR
    $ python app.py      # runs on http://127.0.0.1:5000 by default
"""
from flask import Flask
from pages import pages

# Function that initializes the Flask application and returns the app instance
def create_app():
    app =  Flask(__name__)
    app.register_blueprint(pages.bp)
    return app

# Allows run.py to run directly to start our web application
#app will run on localhost, port 5000
if __name__ == "__main__":
    app = create_app()
    app.run()