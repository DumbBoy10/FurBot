#   FurBot
import nextcord
import os
from nextcord.ext import commands


os.chdir("H:/Python/FurBot")

# Replace with your Nexcord bot token
BOT_TOKEN = open("token.txt", "r").read()
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.reply("Hello!")


# Run the bot
client.run(BOT_TOKEN)
