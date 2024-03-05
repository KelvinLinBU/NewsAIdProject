from openai import OpenAI
from openai import Client
import json
import os
import openai

#run using python3 Backend/chatgpt.py

def ChatGPT_determine_role(style):
    """This is the function in order tomdetermine the role of ChatGPT. Takes a string style and concatenates a starter to it"""
    result = 'You are a '
    result += style
    return result

def ChatGPT_details_not_exceed(details, length):
    """Function to check if the details that a user puts in exceeds length characters. Returns true if it exceeds, false if not"""
    return len(details) > length

def ChatGPT_API_Call_for_Headline(details, style):
    """Function to call ChatGPT API and get headline. Takes user inputted details, and the preferred style and saves it in a headline json file"""
    # Make sure to use the correct environment variable name
    apikey = os.getenv('OPENAI_API_KEY')  #"API Key Environment variable name"
    if apikey is None:
        print("Environment variable not found")
    else:
        print("Environment variable recognized")
    openai.api_key = apikey
    style_choice = ChatGPT_determine_role(style)
    headline = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": style_choice}, #role of chatgpt, Will be set by the user in the future, to be replaced with user saved personality from the front end
        {"role": "user", "content": details} #the user query, this is to get the headline, to be replaced with user input from the front end
    ]
)
    #Save response in a json file
    with open('headline.json', 'w') as file:
        json.dump(headline, file, default=str)  # Use default=str to handle non-serializable data, if any
    print("JSON object saved as headline.json")

def ChatGPT_API_Call_for_ArticleBody(details, style):
    """Function to call ChatGPT API and get headline. Takes user inputted details, and the preferred style and saves it in a headline json file"""
    # Make sure to use the correct environment variable name
    apikey = os.getenv('OPENAI_API_KEY')  #"API Key Environment variable name"
    if apikey is None:
        print("Environment variable not found")
    else:
        print("Environment variable recognized")
    openai.api_key = apikey
    style_choice = ChatGPT_determine_role(style)
    article_body = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": style_choice}, #role of chatgpt, Will be set by the user in the future, to be replaced with user saved personality from the front end
        {"role": "user", "content": details} #the user query, this is to get the article_body, to be replaced with user input from the front end
    ]
)
#Save response in a json file
    with open('article_body.json', 'w') as file:
        json.dump(article_body, file, default=str)  # Use default=str to handle non-serializable data, if any
    print("JSON object saved as article_body.json")

