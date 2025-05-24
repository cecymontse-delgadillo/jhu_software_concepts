from flask import Blueprint, render_template

#create a blueprint instance named bp that uses
#  the template folder under app folder
bp = Blueprint("pages", __name__)

# A decorator used to tell the app home URL is 
# associated to this function that returns template home.html
@bp.route("/")
def home():
    return render_template("home.html", current_page="home")

# A decorator used to tell the app home URL is 
# associated to this function
@bp.route("/contact")
def contact():
    return render_template("contact.html", current_page="contact")

@bp.route("/projects")
def projects():
    return render_template("projects.html", current_page="projects")