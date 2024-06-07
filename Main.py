import discord
from discord.ext import commands
import os

# Initialize bot
bot = commands.Bot(command_prefix='!')

# Gets the bot token and API key, export your token and key in terminal to store them locally.
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.command(name='ask')
async def ask(ctx, *, question: str):
    await ctx.send("Sorry, this feature is not available.")

# Run bot
bot.run(DISCORD_TOKEN)
