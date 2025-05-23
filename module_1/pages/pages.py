from flask import Blueprint, render_template

#create a blueprint instance named bp that uses
#  the template folder under app folder
bp = Blueprint("pages", __name__)

# A decorator used to tell the app the URL is 
# associated to a function
@bp.route("/")
def home():
    return render_template("home.html")