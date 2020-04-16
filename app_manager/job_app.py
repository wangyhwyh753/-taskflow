
from flask import Flask, request


manager = Flask(__name__)


@manager.route('/submit', methods=["POST","GET"])
def submit_job():
    job_name = request.json.get["job_name"]
    job_config = request.json.get["job_config"]