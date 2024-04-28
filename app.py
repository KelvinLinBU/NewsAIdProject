from flask import Flask, render_template, session, redirect, request, abort
from functools import wraps
import pymongo
import cred
import os
import pathlib


import requests 
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
app = Flask(__name__)
#generate secret key

app.secret_key = cred.FLASK_SECRET_KEY
GOOGLE_CLIENT_ID = cred.GOOGLE_ID
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],


    # redirects to the callback uri
    redirect_uri="http://127.0.0.1:5000/callback"

   
)
#Initiating Database to localhost
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system





#Decorate
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session or 'google_id' in session:
            return f(*args, **kwargs)

        else:
            return redirect('/account')
    return wrap



# Routes
from user import route 
@app.route('/account')
def home():
    return render_template('home.html')

@app.route("/googlelogin")
def googlelogin():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/dashboard/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/account")




@app.route('/dashboard/')
#intercepts redirecting to dashboard with login
@login_required
def dashboard():
    return render_template('newsformpage.html')

