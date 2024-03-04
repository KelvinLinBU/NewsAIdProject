from openai import OpenAI
from openai import Client
import json
import os
import openai

#run using python3 Backend/chatgpt.py

# Make sure to use the correct environment variable name
apikey = os.getenv('OPENAI_API_KEY')  #"API Key Environment variable name"
if apikey is None:
    print("Environment variable not found")
else:
    print("Environment variable recognized")
openai.api_key = apikey

headline = openai.chat.completions.create(
   model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an assistant to an unbiased journalist."}, #role of chatgpt, Will be set by the user in the future, to be replaced with user saved personality from the front end
        {"role": "user", "content": "write a newsheadline on mayor bob's fraud scandal"} #the user query, this is to get the headline, to be replaced with user input from the front end
    ]
)

#Save response in a json file
with open('headline.json', 'w') as file:
    json.dump(headline, file, default=str)  # Use default=str to handle non-serializable data, if any

print("JSON object saved as headline.json")

article_body = openai.chat.completions.create(
   model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an assistant to an unbiased journalist."}, #role of chatgpt, Will be set by the user in the future, to be replaced with user saved personality from the front end
        {"role": "user", "content": "write a 100 word article on mayor bob's fraud scandal"} #the user query, this is to get the article_body, to be replaced with user input from the front end
    ]
)

#Save response in a json file
with open('article_body.json', 'w') as file:
    json.dump(article_body, file, default=str)  # Use default=str to handle non-serializable data, if any

print("JSON object saved as article_body.json")

