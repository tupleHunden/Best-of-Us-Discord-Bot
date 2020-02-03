# General Bot for the Discord Server Best of Us
# Join over at discord.gg/BestOfUs

# TODO LIST
# 1. Random Dadjoke
# 2. Remind me
# 3. Add some moderation features

import os
import discord
import requests
from dotenv import load_dotenv
from datetime import datetime
from discord.ext import commands

# Load the .env file with our authentication token.
# For local installation be sure to create your own .env file.
# It should contain DISCORD_TOKEN=input_your_oauth_token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# This will enable the prefix ~ for users to issue commands to the bot.
# e.g. = ~time, ~date, etc.
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
        f'Hello {member.name}, welcome to Best of Us!  You should see our #server-info, #announcements, #suggestions, and #welcome-mat channels upon joining.'  
        f'Check out #server-info first, it will guide you through some information about us and how the server works.  When you feel comfortable with the rules, check out #welcome-mat to get your roles set up.  Just press whichever emoji describes you best.'  
        f'For most it will be the EVE and Veteran roles.'  
        f'If you have any questions at all, please let one of the admins know, we are at the top of the member list.'  
        f'Thanks! ~Alchemist8'
    )

# Commands Section - All bot commands will be included here.

# Tells the user the current time in EVE Online based on ~time command.
@bot.command(name='time', help='This command displays the current EVE Online time.')
async def eve_time(ctx):
    utc_time = datetime.utcnow()
    timeStr = utc_time.strftime("%H:%M:%S")
    
    time_in_eve = "The current time in EVE is %s" % timeStr
    await ctx.send(time_in_eve)

# Gives the user a link to the current BAH Calculator based on ~bah.
@bot.command(name='bah', help='This command will post a link to the current Basic Allowance for Housing (BAH) calculator.')
async def bah_calc(ctx):
    give_bah = 'https://www.defensetravel.dod.mil/site/bahCalc.cfm'

    await ctx.send(give_bah)

# Provides the user with an invite link to the Best of Us server.
@bot.command(name='invite', help='This command will post an invite link to the server.')
async def invite_link(ctx):
    invite = 'https://discord.gg/bestofus'

    await ctx.send(invite)

# Provides the user with a link to the Terminal Lance comic for the day.
# Will update in the future to provide a link to a random TL Comic.
@bot.command(name='tl', help='This command will post a link to the Terminal Lance website.')
async def terminal_lance(ctx):
    tl_comic = 'https://terminallance.com'

    await ctx.send(tl_comic)

# Provides the user with the current EVE Online server status.
@bot.command(name='eve', help='This command will post the current EVE Online server status.')
async def eve_status(ctx):
    response = requests.get('https://esi.evetech.net/latest/status/?datasource=tranquility')
    server_status = response.json()

    await ctx.send(server_status)

# Provides the user with some information on the Discord server.
@bot.command(name='info', help='This command gives the user some basic info about the Discord server.')
async def info(ctx ):
    embed = discord.Embed(title='Best of Us', description='Best of Us is a community project for Military Veterans in Eve Online from across the world to come together and find a sense of belonging')
    embed.add_field(name='Member Count', value=f'{len(bot.guilds)}')

    await ctx.send(embed=embed)

# Provides the user a link to the GitHub repo.
@bot.command(name='github', help='This command provides the user with a link to the GitHub Repo.')
async def github_repo(ctx):
    github = 'https://github.com/tupleHunden/Best-of-Us-Discord-Bot'

    await ctx.send(github)

# Auto Loan Calculator
@bot.command(name='carloan', help='This command is a simple tool for calculating auto loan payments.')
async def carloan(ctx):
    loanMonths = input('Enter the loan length in months: ')
    loanInterest = input('Enter the interest of the loan in decimals: ')
    loanAmount = input('Enter the cash amount of the loan: ')

    totalLoan = loanMonths + loanInterest + loanAmount

    carloan = totalLoan

    await ctx.send(carloan)

bot.run(token)