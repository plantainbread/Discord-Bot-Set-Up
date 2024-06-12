from app.discord_bot.discord_api import client, discord_token

if __name__ == '__main__':
    client.run(discord_token)

#Current issue: code allows me to import client, but not discord_token.
