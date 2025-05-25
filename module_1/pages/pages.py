"""
pages.py - Route Definitions via Flask Blueprint
-------------------------------------------------
This module defines a Flask Blueprint named `pages` which includes
routes for rendering various pages of the personal website.
Features:
- Uses templates for dynamic HTML rendering
- Defines routes for the Home, Contact, and Projects pages
- Passes `current_page` context to templates for navigation highlighting
This module is registered in the main Flask app via `app.register_blueprint(pages.bp)` in run.py.
"""
from flask import Blueprint, render_template

# Create a blueprint instance named 'bp'
# Uses the 'template' folder to load HTML
bp = Blueprint("pages", __name__)

# A decorator that defines a route to home page
@bp.route("/")
def home():
    return render_template("home.html", current_page="home")

# A decorator that defines a route to contact page
@bp.route("/contact")
def contact():
    return render_template("contact.html", current_page="contact")

# A decorator that defines a route to projects page
@bp.route("/projects")
def projects():
    return render_template("projects.html", current_page="projects")