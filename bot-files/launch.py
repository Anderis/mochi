import discord
from discord.ext import commands
import bot
import mochiResponses as responses
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    load_dotenv()  # Load environment variables from .env file
    mochiResponses = responses  # Pass the responses module to the bot module
    bot_token = os.getenv('DISCORD_TOKEN')  # Retrieve bot token from environment variables
    bot.run_discord_bot(bot_token)
