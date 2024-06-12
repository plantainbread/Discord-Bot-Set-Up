import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

#configure the model used in this bot.
#The return statement is used to only access the content key value pair because the model response in a json file format.
#Refer to the OpenAI API reference, making requests section if you want to see it visualized.
def gpt_response(prompt):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo', 
            message=[{"role": "user", "content": prompt}]
            )
        return response.choices[0].message.content.strip()
