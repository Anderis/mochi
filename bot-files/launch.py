import discord
from discord.ext import commands
import bot
import mochiResponses as responses

if __name__ == '__main__':
    bot.responses = responses  # Pass the responses module to the test_bot module
    bot.run_discord_bot()