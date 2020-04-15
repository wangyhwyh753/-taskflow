from flask import Flask, render_template
from flask import request
from werkzeug.wsgi import DispatcherMiddleware
from app_manager import job_app, data_app

manager = Flask(__name__)

@manager.route('/register',methods=['GET','POST'])
def register():
    if request == 'GET':
        return render_template('register.html')
    else:
        uname =request.form['username']
        email=request.form['email']
        uurl=request.form['url']
        upwd=request.form['password']
        return render_template('login.html')

if __name__ == "__main__":
    app = DispatcherMiddleware(manager,{"/data":data_app,"/job":job_app})