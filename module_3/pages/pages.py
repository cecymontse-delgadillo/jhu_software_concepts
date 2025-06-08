from flask import Blueprint, render_template
from query_data import GrandCafeAnalysis

# Create a blueprint instance named 'bp'
# Uses the 'template' folder to load HTML
bp = Blueprint("pages", __name__)

# A decorator that defines a route to home page
@bp.route("/")
def index():
    questions = GrandCafeAnalysis().execute_analysis()
    return render_template("questions.html", questions=questions)

