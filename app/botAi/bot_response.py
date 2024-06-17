from openai import OpenAI
import os
from dotenv import load_dotenv

api_key2 = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def gpt_response(prompt):
    chat_completion = api_key2.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        # You may change the model if you like to something else such as gpt-4o, you can see the options on the OpenAI API site.
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content.strip()
