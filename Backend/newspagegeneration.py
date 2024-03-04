from flask import Flask, render_template
import os

#run this using command in the terminal: python3 Backend/newspagegeneration.py
#then, go to this link in your browser: http://127.0.0.1:5000/

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates_dir = os.path.join(BASE_DIR, 'Frontend', 'templates')
static_dir = os.path.join(BASE_DIR, 'Frontend', 'static')
print("Base directory:", BASE_DIR)
print("Template directory:", templates_dir)
print("Static directory:", static_dir)

app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)

# Dummy data for a blog post
blog_post = {
    "title": "News Article", #this should be extracted form the header json file
    "posted_on": "March 4, 2024", #date
    "content": "This is a great blog post. It contains a lot of useful information about web development, including how to build dynamic websites using HTML, CSS, and JavaScript. Enjoy reading!" #extracted from article_body.json
    
}

@app.route("/")
def home():
    return render_template("newspage.html", post=blog_post)

if __name__ == "__main__":
    app.run(debug=True)