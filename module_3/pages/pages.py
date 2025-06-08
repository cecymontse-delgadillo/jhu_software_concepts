"""
pages.py - Route Definitions via Flask Blueprint
-------------------------------------------------
This module defines a Flask Blueprint named `pages` which includes
routes for rendering various pages of the personal website.
Features:
- Uses templates for dynamic HTML rendering
- Defines routes for index
- This module is registered in the main Flask app via `app.register_blueprint(pages.bp)` in app.py.
"""
from flask import Blueprint, render_template
from query_data import GrandCafeAnalysis

# Create a blueprint instance named 'bp'
# Uses the 'template' folder to load HTML
bp = Blueprint("pages", __name__)

# A decorator that defines a route to index page
@bp.route("/")
def index():
    questions = GrandCafeAnalysis().execute_analysis()
    return render_template("questions.html", questions=questions)

