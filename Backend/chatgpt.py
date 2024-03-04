from openai import OpenAI
from openai import Client
import json
import os
import openai

# Make sure to use the correct environment variable name
apikey = os.getenv('OPENAI_API_KEY')  #"API Key Environment variable name"
if apikey is None:
    print("Environment variable not found")
else:
    print("Environment variable recognized")
openai.api_key = apikey

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the World Series in 2020?"}
    ]
)

#Save response in a json file
with open('response.json', 'w') as file:
    json.dump(response, file, default=str)  # Use default=str to handle non-serializable data, if any

print("JSON object saved as response.json")
