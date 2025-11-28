from flask import Blueprint, render_template
from .models import Logs

pages = Blueprint("pages", __name__)

# Landing Page
@pages.get("/")
def landing_page():
    return render_template("landing.html")

# Logs page (show all logs)
@pages.get("/personal-logs")
def logs_page():
    logs = Logs.query.order_by(Logs.id.desc()).all()
    return render_template("logs.html", logs=logs)