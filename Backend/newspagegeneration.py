from flask import Flask, render_template, request, redirect, url_for, session
import os
import chatgptfuncs #from chatgptfuncs.py


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
def newsforms():
    # Serve the submission form
    return render_template('newsformpage.html')

@app.route('/submit-form', methods=['POST']) #find submit form
def submitforms():
    # Extract the submitted data and store it in session
    style = request.form['style']
    session['style'] = style  # Store style in session
    details = request.form['articledetails']
    session['details'] = details #Store details in session 
    
    #Want to call chatGPT here, write chatGPT helper functions
    # Redirect to the result page
    return redirect(url_for('newspage'))

@app.route("/newspage")
def newspage():
    category_style = session.get('style', 'No Input Provided')  # Safely get style session data
    
    print(category_style)  
    details = session.get('details', 'No Input Provided')  # Safely get details session data
    chatgptfuncs.ChatGPT_API_Call_for_Headline(details, category_style) #create json file with generated headline
    chatgptfuncs.ChatGPT_API_Call_for_ArticleBody(details, category_style, 100) #create json file with generated content
    headline = chatgptfuncs.extract_from_json_file("headline.json")
    article_body = chatgptfuncs.extract_from_json_file("article_body.json")
    print(details)  
    dynamic_post = { #dynamic blog post
        "title": headline,  # Example title modification
        "posted_on": "March 4, 2024",  # You might want this to be dynamic as well
        "content": article_body  # Use the details from the form as the article content
    }
    return render_template("newspage.html", post=dynamic_post)

if __name__ == "__main__":
    app.run(debug=True)



# Example usage
#file_path = 'response.json'  # The path to your JSON file
#key_path = ['choices', 0, 'message', 'content']  # The path to the desired content
#content = extract_content_from_json_file(file_path, key_path)
#print("Extracted content:", content)