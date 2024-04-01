from openai import OpenAI
from openai import Client
import json
import os
import openai
import re
import ast

#run using python3 Backend/chatgpt.py

def ChatGPT_determine_role(style, factorembellish):
    """This is the function in order tomdetermine the role of ChatGPT. Takes a string style and concatenates a starter to it
    takes "factual" or "embellish" 
    """
    print(factorembellish)
    result = 'You are a '
    result += style
    result += ' who writes fictional news articles for a creative purpose.'
    if factorembellish == "Factual":
        print("Factual")
        result += ' You must keep it factual. Follow the prompt exactly'
    if factorembellish == "Embellish":
        print("Embellished")
        result += ' You are able to embellish the article.'
    return result

def ChatGPT_details_not_exceed(details, length):
    """Function to check if the details that a user puts in exceeds length characters. Returns true if it exceeds, false if not"""
    return len(details) > length

def ChatGPT_API_Call_for_Headline(details, style, factorembellish):
    """Function to call ChatGPT API and get headline. Takes user inputted details, and the preferred style and saves it in a headline json file"""
    # Make sure to use the correct environment variable name
    apikey = os.getenv('OPENAI_API_KEY')  #"API Key Environment variable name"
    if apikey is None:
        print("Environment variable not found")
    else:
        print("Environment variable recognized")
    openai.api_key = apikey
    style_choice = ChatGPT_determine_role(style, factorembellish)
    headline = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": style_choice}, #role of chatgpt, Will be set by the user in the future, to be replaced with user saved personality from the front end
        {"role": "user", "content": "using these details, create a headline " + details + ". Keep it to a max of 10 words"} #the user query, this is to get the headline, to be replaced with user input from the front end
    ]
)
    #Save response in a json file
    with open('headline.json', 'w') as file:
        json.dump(headline, file, default=str)  # Use default=str to handle non-serializable data, if any
    print("JSON object saved as headline.json")

def ChatGPT_API_Call_for_ArticleBody(details, style, length, factorembellish):
    """Function to call ChatGPT API and get headline. Takes user inputted details, and the preferred style and saves it in a headline json file"""
    # Make sure to use the correct environment variable name
    apikey = os.getenv('OPENAI_API_KEY')  #"API Key Environment variable name"
    if apikey is None:
        print("Environment variable not found")
    else:
        print("Environment variable recognized")
    openai.api_key = apikey
    style_choice = ChatGPT_determine_role(style, factorembellish)
    article_body = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": style_choice}, #role of chatgpt, Will be set by the user in the future, to be replaced with user saved personality from the front end
        {"role": "user", "content": "Write for me a " + str(length) + "word newspaper article using the following details: " + details} #the user query, this is to get the article_body, to be replaced with user input from the front end
    ]
)
#Save response in a json file
    with open('article_body.json', 'w') as file:
        json.dump(article_body, file, default=str)  # Use default=str to handle non-serializable data, if any
    print("JSON object saved as article_body.json")

def extract_generated_text(response_str):
    # Regular expression to extract the content within 'content=' and the next single quote
    match = re.search(r"content='(.*?)'", response_str)
    if match:
        return match.group(1)
    else:
        return None

def extract_from_json_file(file_path):
    try:
        # Open and read the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            #json_string = file.read()  # Read the content of the file as a string
                json_string = file.read()
        print(json_string)
        json_data = json.loads(json_string)
        print(json_data)
        #response_obj = ast.literal_eval(json_data)
        
        
        # Navigate through the data structure to extract the content
        content = extract_generated_text(json_string)
        #content = response_obj.choices[0].message.content
        
        # Return the extracted content
        return content
    except (KeyError, IndexError, json.JSONDecodeError, json.JSONDecodeError) as error:
        print(f"Error extracting content: {error}")
        return None

