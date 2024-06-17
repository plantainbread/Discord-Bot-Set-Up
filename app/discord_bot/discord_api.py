import discord
from app.botAi.bot_response import gpt_response
from dotenv import load_dotenv
import os

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN_KEY")

class MyClient(discord.Client):

    async def on_ready(self):
        print("Logged in as", self.user)
    
    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return
        command, user_message=None, None
    # You may change the commands to anything you like, though you have to update the if statements below.
        for text in ['/bot','/ask','/chat']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print(command, user_message)
    # You have to change this if you wish to alter the commands, I probably could have done this more efficiently but it is what it is.
        if command == '/bot' or command == '/ask' or command == '/chat':
            bot_response = gpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")
    
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
