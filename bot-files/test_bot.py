import discord
import test_responses as responses
from discord.ext import commands
import re
import random
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
    bot = commands.Bot(command_prefix='!', intents=intents.all(), help_command=None)  # Disable the default help command

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

        if re.search(r'\bwoof\b', user_message, re.IGNORECASE):
            image_url = "https://cdn.discordapp.com/attachments/1112267773679255552/1112467523770789959/image.png"
            embed = discord.Embed()
            embed.set_image(url=image_url)
            embed.color = discord.Color.yellow()
            embed.description = '**WOOF!**'
            await message.channel.send(embed=embed)
        elif re.search(r'\btreat\b', user_message, re.IGNORECASE):
            image_url = "https://media.discordapp.net/attachments/1112267773679255552/1112978358599422003/treat.gif"
            embed = discord.Embed()
            embed.set_image(url=image_url)
            embed.color = discord.Color.yellow()
            embed.description = '*`... Mochi perks up at the word treat ...`*'  # Set the description
            await message.channel.send(embed=embed)
            await send_message(message, user_message, is_private=True)
        elif re.search(r'\bsquirrel\b', user_message, re.IGNORECASE):
            image_url = "https://cdn.discordapp.com/attachments/1112267773679255552/1112994685204578304/giphy_1.gif"
            embed = discord.Embed()
            embed.set_image(url=image_url)
            embed.color = discord.Color.yellow()
            embed.description = '***`... MOCHI PERFORMS THE ZOOMIES ...`***'
            await message.channel.send(embed=embed)
        else:
            await send_message(message, user_message, is_private=False)

        await bot.process_commands(message)  # Process commands after checking messages

    @bot.command(name='mochihelp', aliases=['help'])
    async def mochihelp_command(ctx):
        embed = discord.Embed(title='MOCHI TO THE RESCUE!', description='List of available commands & phrases:', color=discord.Color.yellow())

        # Commands
      
        commands_field = "A command can only be run standalone and must begin with a \"!\".\n"
        commands_field += "```"
        commands_field += "[!mochihelp, !help]  Help Document.\n"
        commands_field += "[!givetreat(s)]  Gives Mochi a treat.\n"
        commands_field += "[!howgay] See how gay you are.\n"
        commands_field += "[!boop] Boops the snoot.\n"
        commands_field += "[!sit] Ask Mochi to sit."
        commands_field += "```"

        embed.add_field(name='__**COMMANDS**__', value=commands_field, inline=False)

        # Trigger Statements
        statements_field = "Similar to commands, a trigger statement cannot include additional characters. However, it does not need to begin with a \"!\".\n"
        statements_field += "```"
        statements_field += "hello\n"
        statements_field += "mochi\n"
        statements_field += "good girl\n"
        statements_field += " "
        statements_field += "```"

        # Trigger Words
        words_field = "A trigger word can be used at any point in a sentence without the need for a prefix.\n"
        words_field += "\n"
        words_field += "```\n"
        words_field += "woof\n"
        words_field += "treat\n"
        words_field += "squirrel"
        words_field += "```"

        embed.add_field(name='__**TRIGGER STATEMENTS**__', value=statements_field, inline=True)
        embed.add_field(name='__**TRIGGER WORDS**__', value=words_field, inline=True)

        await ctx.send(embed=embed)

        


    @bot.command(name='boop')
    async def boop_command(ctx):
            image_url = "https://cdn.discordapp.com/attachments/1011343025659727894/1093730940653674496/20230406_195355_1.gif"
            embed = discord.Embed()
            embed.set_image(url=image_url)
            embed.color = discord.Color.yellow()
            embed.description = '***`... MOCHI ATTACKS!!! ...`***'
            await ctx.send(embed=embed)

    @bot.command(name='givetreat', aliases=['givetreats'])
    async def givetreat_command(ctx):
            image_url = "https://cdn.discordapp.com/attachments/1112267773679255552/1112974425369878589/202305300010.gif"
            embed = discord.Embed()
            embed.set_image(url=image_url)
            embed.color = discord.Color.yellow()
            embed.description = '**`... Mochi happily eats her treats ...`**'
            await ctx.send(embed=embed)

    @bot.command(name='howgay')
    async def howgay_command(ctx):
        image_url = "https://media.discordapp.net/attachments/1112267773679255552/1112735249814790204/png_20230407_124312_0000.png?width=509&height=905"
        percentage = str(random.randint(0, 100))
        embed = discord.Embed()
        embed.set_image(url=image_url)
        embed.color = discord.Color.yellow()
        embed.description = "*Wise bunny sage Mochi declares that you are .......* **" + percentage + "% GAY!**"
        await ctx.send(embed=embed)
    
    @bot.command(name='sit')
    async def sit_command(ctx):
         #needs image embed added later
         embed = discord.Embed()
         embed.color= discord.Color.yellow()
         embed.description = '**`Mochi sits begrudgingly, awaiting a treat.`**'
         await ctx.send(embed=embed)
    bot.run(TOKEN)
