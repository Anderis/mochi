import discord
import test_responses as responses
from discord.ext import commands
import re

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)

        if response and not is_private:
            await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTExMTkyOTk3NTY0MjI2MzU2Mg.G4VjeC.u_Hnu2cKB-AH0CprF5Iry3kSJQNPVAofjXc1KA'
    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False
    intents.messages = True
    bot = commands.Bot(command_prefix='!', intents=intents.all())

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running')

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f'{username} said: "{user_message}" ({channel})')

        # Use regex to find "woof" regardless of position and capitalization
        if re.search(r'\bwoof\b', user_message, re.IGNORECASE):
            image_url = "https://cdn.discordapp.com/attachments/1112267773679255552/1112467523770789959/image.png"
            embed = discord.Embed()
            embed.set_image(url=image_url)
            await message.channel.send(embed=embed)
        elif user_message.startswith('?'):
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

        await bot.process_commands(message)  # Process commands after checking messages

    bot.run(TOKEN)
