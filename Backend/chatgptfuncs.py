from openai import OpenAI
from openai import Client
import json
import os
import openai
import re
import ast

import requests

#run using python3 Backend/chatgpt.py
def generate_picture_using_headline(headline):
    """Uses the OpenAI API to generate an image based on the headline passed in. Saves the image as generated_image.png."""
    try:
        # Assuming 'openai.Image.create' is the correct method based on the latest API
        image_response = openai.images.generate(
            model ="dall-e-3",
            prompt=headline,
            n=1,  # Number of images to generate
            size="1024x1024",  # Image size, adjust based on your requirements
            quality="standard",
        )
        
        # Assuming the first image is the one we want
        image_url = image_response.data[0].url
        print("Generated Image URL:", image_url)
        
        # Save the Image as a PNG
        image_data = requests.get(image_url).content
        with open("generated_image.png", "wb") as image_file:
            image_file.write(image_data)
        print("Image saved as generated_image.png")
    except Exception as e:
        print(f"An error occurred: {e}")

def ChatGPT_determine_role(style, factorembellish):
    """This is the function in order tomdetermine the role of ChatGPT. Takes a string style and concatenates a starter to it
    takes "factual" or "embellish" 
    """
    print(factorembellish)
    result = 'You are a '
    result += style
    
    result += ' who writes fictional news articles for a creative purpose.'
    if style == 'Standard News Reporter':
        result += ' Keep the tone professional.'
    if style == 'Opinion Columnist':
        result += ' Please include a fictional writers own take.'
    if style == "Feature / Enterprise Reporter":
        result += ' Please keep the tone as if you were a feature or enterprise reporter.'
    if style == "Investigative Reporter":
        result += ' Keep the tone of the story as inquisitive.'
    if factorembellish == "Factual":
        print("Factual")
        result += ' You must keep it factual. Follow the prompt exactly'
    if factorembellish == "Embellish":
        print("Embellished")
        result += ' You are able to embellish the article.'
    return result

 #<option value="Standard News Reporter">Standard News Reporter</option>  <!-- This is the standard unbiased news reporter-->
#            <option value="Opinion Columnist">Opinion Columnist</option> <!-- This is for opinion based writing-->
   #           <option value="Feature / Enterprise Reporter">Feature / Enterprise Reporter</option> <!-- This is for if you want to write a more flowery piece-->
    #          <option value="investigative Reporter">Investigative Reporter</option> <!-- This is for if you want a more investigative piece-->

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
        {"role": "user", "content": "Write for me a " + str(length) + "word newspaper article using the following details: " + details + ". There is no need to include a headline "} #the user query, this is to get the article_body, to be replaced with user input from the front end
    ]
)
#Save response in a json file
    with open('article_body.json', 'w') as file:
        json.dump(article_body, file, default=str)  # Use default=str to handle non-serializable data, if any
    print("JSON object saved as article_body.json")

def extract_from_json_file(file_path):
    try:
        # Open and read the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            json_string = file.read()  # Read the content of the file as a string
        
      
        
        # Navigate through the data structure to extract the content
        content = extract_quoted_strings(json_string)
        
        # Return the extracted content
        return content
    except (KeyError, IndexError, json.JSONDecodeError, json.JSONDecodeError) as error:
        print(f"Error extracting content: {error}")
        return None


def extract_quoted_strings(s):
    # Regular expression pattern to find strings enclosed in \"
    pattern = r"content=(.*?), role='assistant'"
    
    # Use re.search to find the first occurrence of the pattern
    match = re.search(pattern, s)
    
    # If a match is found, return the captured group (the content between the markers)
    # If no match is found, return None or an appropriate message
    if match:
      
        return match.group(1).replace("\\", "").replace("\n\n", "")  # Return the first captured group (content between the markers)
    else:
        return "Content not found or pattern does not match."
# Example usage
#file_path = 'response.json'  # The path to your JSON file
#key_path = ['choices', 0, 'message', 'content']  # The path to the desired content
#content = extract_content_from_json_file(file_path, key_path)
#print("Extracted content:", content)