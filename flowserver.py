from flask import Flask, render_template
from flask import request

app = Flask("flowserver")

@app.route('/register',methods=['GET','POST'])
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
    app.run(host="0.0.0.1",port="8282")