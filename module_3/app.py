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