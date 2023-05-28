import discord
from discord.ext import commands
import test_bot
import test_responses as responses

if __name__ == '__main__':
    test_bot.responses = responses  # Pass the responses module to the test_bot module
    test_bot.run_discord_bot()