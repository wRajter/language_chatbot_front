# more info https://beta.openai.com/examples/default-translate
import os
from urllib import response
import openai
#from dotenv import load_dotenv, find_dotenv

key = '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'

# loading the key from the .env file
#env_path = find_dotenv() # automatic find
#load_dotenv(env_path)
#key = os.getenv('OPENAI_AUTH_KEY')


def bot_translation(text, target_language):
    '''translates the text into the targeted language.
    Please, specify the text you want to translate and language that you want to translate into'''
    openai.api_key = key
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate this into 1. {target_language}:\n\n{text}\n\n1.",
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
    return response['choices'][0]['text']
