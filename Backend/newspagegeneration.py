from flask import Flask, render_template, request, redirect, url_for, session
import os

#Uses FLASK
#run this using command in the terminal: python3 Backend/newspagegeneration.py
#then, go to this link in your browser: http://127.0.0.1:5000/
flaskkey = os.getenv('FLASK_SESSION_KEY')  #"Flask Session Key Environment variable name"
if flaskkey is None:
    print("Environment variable not found")
else:
    print("Environment variable recognized")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates_dir = os.path.join(BASE_DIR, 'Frontend', 'templates')
static_dir = os.path.join(BASE_DIR, 'Frontend', 'static')
print("Base directory:", BASE_DIR)
print("Template directory:", templates_dir)
print("Static directory:", static_dir)

app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
app.secret_key = flaskkey

@app.route('/')
def home():
    # Serve the submission form
    return render_template('newsformpage.html')

# Dummy data for a blog post
blog_post = {
    "title": "News Article", #this should be extracted form the header json file
    "posted_on": "March 4, 2024", #date
    "content": "This is a great blog post. It contains a lot of useful information about web development, including how to build dynamic websites using HTML, CSS, and JavaScript. Enjoy reading!" #extracted from article_body.json
    
}

@app.route('/submit-form', methods=['POST'])
def submitforms():
    # Extract the submitted data and store it in session
    style = request.form['style']
    session['style'] = style  # Store data in session
    details = request.form['articledetails']
    session['details'] = details
    # Redirect to the result page
    return redirect(url_for('newspage'))

@app.route("/newspage")
def newspage():
    category_style = session.get('style', 'No Input Provided')  # Safely get session data
    print(category_style)  
    details = session.get('details', 'No Input Provided')  # Safely get session data
    print(details)  
    return render_template("newspage.html", post=blog_post)

if __name__ == "__main__":
    app.run(debug=True)



