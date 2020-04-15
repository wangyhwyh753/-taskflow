
from flask import Flask, request


manager = Flask(__name__)

@manager.route("/submit",methods=["post"])
def submit_job():
    job_name = request.get["job_name"]
    job_config = request.get["job_config"]