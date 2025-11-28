from flask import Blueprint, request, jsonify
from . import db
from .models import Logs

api = Blueprint("api", __name__)

# List all logs
@api.get("/logs")
def get_logs():
    logs = Logs.query.order_by(Logs.id.desc()).all()
    return jsonify([log.to_dict() for log in logs])


# Get a single log by ID
@api.get("/logs/<int:log_id>")
def get_log(log_id):
    log = Logs.query.get_or_404(log_id)
    return jsonify(log.to_dict())


# Create a new log entry
@api.post("/logs")
def create_log():
    data = request.get_json()

    new_log = Logs(
        log=data["log"],
        author=data["author"]
    )

    db.session.add(new_log)
    db.session.commit()

    return jsonify(new_log.to_dict()), 201


# Delete a log by ID
@api.delete("/logs/<int:log_id>")
def delete_log(log_id):
    log = Logs.query.get_or_404(log_id)
    db.session.delete(log)
    db.session.commit()
    return {"deleted": True}