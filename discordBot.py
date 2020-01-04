# General Bot for the Discord Server Best of Us
# Join over at discord.gg/BestOfUs
# Built by tupleHunden (GitHub.com/tupleHunden)

import os
import discord
from dotenv import load_dotenv
from datetime import datetime
from discord.ext import commands

# Load the .env file with our authentication token.
# For local installation be sure to create your own .env file.
# It should contain DISCORD_TOKEN=input_your_oauth_token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# This will enable the prefix ~ for users to issue commands to the bot.
# e.g. = !time, !date, etc.
bot = commands.Bot(command_prefix='~')

# Displays a terminal message when the bot connects.
@bot.event
async def on_ready():
    print(f'{bot.user} has successfully connected to Discord.')

# When someone joins the discord server, the bot will welcome them.
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, welcome to Best of Us.  Be sure to check out our server info and welcome mat channels.  If you need any assistance with roles or have questions at all, let one of the Admin staff know. - Alch'
    )

# Commands Section - All bot commands will be included here.

# Tells the user the current time in EVE Online based on ~time command.
@bot.command(name='time', help='This command displays the current EVE Online time.')
async def eve_time(ctx):
    utc_time = datetime.utcnow()
    timeStr = utc_time.strftime("%H:%M:%S")
    
    response = "The current time in EVE is %s" % timeStr
    await ctx.send(response)

# Gives the user a link to the current BAH Calculator based on ~bah.
@bot.command(name='bah', help='This command will post a link to the current Basic Allowance for Housing (BAH) calculator.')
async def bah_calc(ctx):
    give_bah = ('https://www.defensetravel.dod.mil/site/bahCalc.cfm')

    await ctx.send(give_bah)

bot.run(token)