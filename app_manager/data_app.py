from flask import Flask, request


manager = Flask(__name__)

@manager.route("/upload",methods=["post"])
def upload_data():
    job_name = request.get["job_name"]
    job_config = request.get["job_config"]