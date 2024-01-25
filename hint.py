import openai
import os
import sys
from dotenv import load_dotenv

load_dotenv() # load variables from the .env file
api_key = os.getenv("API_KEY")

def hint(question):
    # Set up the OpenAI API key
    openai.api_key = api_key

    # Set the prompt
    prompt = "give me a hint for this question : "+ question +" ."

    # Generate the text
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    temperature=0.5,
    max_tokens=1000,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
    )

    body = response.choices[0].text
    print(body)
    
# Check if an argument was provided
if len(sys.argv) > 1:
    # Get the argument and call the hint function
    question = sys.argv[1]
    hint(question)
else:
    print("Please provide a question as an argument.")
