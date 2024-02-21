#   FurBot
import nextcord
import random
import os
from nextcord.ext import commands


os.chdir("H:/Python/FurBot")
BOT_TOKEN = open("token.txt").read()


# Create a Nexcord client
client = nextcord.Client()

# Define basic commands
@client.event
async def on_message(message):
    if message.author == client.user:  # Prevent bot from responding to itself
        return

    if message.content.startswith("!hello"):
        await message.channel.send("Hello there!")

    elif message.content.startswith("!ping"):
        await message.channel.send("Pong!")

    elif message.content.startswith("!help"):
        help_message = """
        **Available commands:**

        - !hello: Greet the bot.
        - !ping: Check the bot's response time.
        - !help: Display this help message.

        **Additional features:**

        - This bot can be expanded to include more commands and functionalities.
        - Consider using error handling and input validation for robustness.
        - Explore Nexcord's documentation for more customization options.
        """
        await message.channel.send(help_message)

# Run the bot
client.run(BOT_TOKEN)
