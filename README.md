# DiscordBot
My first project yay :D

SET UP NOTE (sorry for yelling):<br>
This is for whoever wants to also create their own bot that can respond back using GPT 3.5.

Download all the files and open them using an IDE. (I used vscode)

Obtain a bot token from the Discord Developer Portal (search it up)<br>
Add the bot to a server of your choice, preferably testing in a private server.
Pay 5 bucks for credits to send requests to use the OpenAI API, otherwise you will receive ErrorCode 429: You exceeded your current quota. <br>
Be sure to generate a new API key after paying and update it in the env file (do not share the Discord Token or API key with anyone else)

If you somehow receive a free trial for the API then you do not need to pay.

(add those into the TokenAndKey.env file)

Don't forget to pip install dotenv, discord, and openai modules.

Once everything is done, run the run.py file and if successful you will see the message 'logged in as (bot name)' in the terminal.

Then, you may type questions in the Discord server for the bot to answer following the set command. E.g. /bot, /ask, /chat.

Side note, if you update any of the files in botAi or discord_bot, make sure to run them before you run main.py.
