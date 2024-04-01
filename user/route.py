from flask import Flask
from app import app
from user.models import User

#  route for signup
@app.route('/user/signup', methods=['POST'])
def signup():
   
    return User().signup()

#  route for signout
@app.route('/user/signout')
def signout():
    return User().signout()

# route for login
@app.route('/user/login', methods=['POST'])
def login():
    return User().login()