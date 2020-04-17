from flask import Flask, request


manager = Flask(__name__)
@manager.route("/upload",methods=["POST","GET"])
def upload_data():
    job_name = request.get["job_name"]
    job_config = request.get["job_config"]