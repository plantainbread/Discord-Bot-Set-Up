from app.discord_bot.discord_api import client, discord_token

if __name__ == '__main__':
    client.run(discord_token)

#problem is that it doesn't let me import my own modules from the left, but the external ones work just fine.