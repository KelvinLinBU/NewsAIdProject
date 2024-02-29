from openai import OpenAI
from openai import Client
import json

apikey = ''
client = OpenAI(api_key=apikey)

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": "Who won the World Series in 2020?"}
    ]
)
response_content = response.choices[0].message.content
# Save the response JSON to a file in the current directory
with open('response.json', 'w') as file:
    json.dump(response_content, file)

print("JSON object saved as response.json")