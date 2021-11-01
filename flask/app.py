from flask import Flask, request
from resources import PasswordManagement

app = Flask(__name__)

pm = PasswordManagement("passwords.json") # ENV

@app.route("/passwords", methods=["GET"])
def pw_list():
    # Call a method to list all passwords
    return pm.list()


@app.route("/passwords/<pw_id>", methods=["GET"])
def pw_get(pw_id):
    # Call a method to list all passwords
    return pm.get(pw_id)


@app.route("/passwords", methods=["POST"])
def pw_post():
    # Validate json
    return "All passwords in json format"


@app.route("/passwords/<pw_id>", methods=["PUT"])
def pw_update():
    # Validate json
    return "All passwords in json format"


@app.route("/passwords/<pw_id>", methods=["DELETE"])
def pw_delete(pw_id):
    pm.delete(pw_id)
    return "Successfully deleted"
