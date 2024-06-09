import discord
from botAi.bot_response import gpt_response
from dotenv import load_dotenv
import os

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):

    async def on_read(self):
        print(self.user,"is alert")
    
    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return
        command, user_message=None, None
    
        for text in ['/bot','/ask','/Bo\'oh\'o\'wa\'er']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.replace(text, '')
                print(command, user_message)

        if command == '/bot' or command == '/ask' or command == '/Bo\'oh\'o\'wa\'er':
            bot_response = gpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")
    
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)