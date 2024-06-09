import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def gpt_response(prompt):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo', 
            message=[{"role": "user", "content": prompt}]
            )
        return response.choices[0].message.content.strip()