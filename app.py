from flask import Flask, render_template
import pymongo
app = Flask(__name__)
#generate secret key
app.secret_key = b'-\x04\xfd\xbb)A\xa2\x06G\x94"f\x00+1L\x1f)'

#Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system
# Routes
from user import route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

