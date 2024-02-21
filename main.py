#   FurBot
import nextcord
import os
from nextcord.ext import commands


os.chdir("H:/Python/FurBot")

# Replace with your Nexcord bot token
BOT_TOKEN = open("token.txt", "r").read()

# Create a Nexcord client
client = nextcord.Client()

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')


# Run the bot
client.run(BOT_TOKEN)
