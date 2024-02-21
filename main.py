#   FurBot
import nextcord
import os

os.chdir("H:/Python/FurBot")

# Replace with your Nexcord bot token
BOT_TOKEN = open("token.txt", "r").read()

# Create a Nexcord client
client = nextcord.Client()


# Define slash commands
@client.slash_command(name="hello", description="Greet the bot")
async def hello(interaction):
    await interaction.response.send_message("Hello there!")


@client.slash_command(name="ping", description="Check the bot's response time")
async def ping(interaction):
    await interaction.response.send_message("Pong!")


@client.slash_command(name="help", description="Display help message")
async def help(interaction):
    help_message = """
    **Available commands:**

    - /hello: Greet the bot.
    - /ping: Check the bot's response time.
    - /help: Display this help message.

    **Additional features:**

    - This bot can be expanded to include more commands and functionalities.
    - Consider using error handling and input validation for robustness.
    - Explore Nexcord's documentation for more customization options.
    """
    await interaction.response.send_message(content=help_message, ephemeral=True)


# Run the bot
client.run(BOT_TOKEN)
