from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo
app = Flask(__name__)
#generate secret key
# WILL BE REMOVED AFTER ALPHA TESTING
app.secret_key = b'-\x04\xfd\xbb)A\xa2\x06G\x94"f\x00+1L\x1f)'

#Initiating Database to localhost
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system

#Decorate
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap
# Routes
from user import route 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
#intercepts redirecting to dashboard with login
@login_required
def dashboard():
    return render_template('dashboard.html')

