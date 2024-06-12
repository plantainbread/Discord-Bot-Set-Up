import discord
from botAi.bot_response import gpt_response
from dotenv import load_dotenv
import os
#Used to access the TokenAndKey.env file and access the discord token
load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    #Show that bot is reading
    async def on_read(self):
        print(self.user,"is alert")
    
    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return
        command, user_message=None, None
        
        #change the different chat commands in the list if you want to customize it.
        for text in ['/bot','/ask','/chat']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.replace(text, '')
                print(command, user_message)
    
        #Don't forget to change these ones too if you want to alter the above
        #There's probably a more efficient way to just iterate over the text list but I am going to change that later.
        if command == '/bot' or command == '/ask' or command == '/chat':
            bot_response = gpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")
    
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
