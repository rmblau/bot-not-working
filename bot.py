# bot.py
from logging import error
import os
import discord
import traceback
import sys 
from discord import client
from discord.ext.commands.errors import BadArgument, CommandError, MemberNotFound, MissingPermissions, MissingRequiredArgument
from discord.ext import tasks  
from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Getting Created!'))
    print(f'{client.user.name} has connected to Discord!')


@client.event  
async def on_command_error(ctx, error):
    if isinstance(error,MemberNotFound):
        await ctx.send("Member not found")
    elif isinstance(error,MissingPermissions):
        await ctx.send("You do not have permission")   
    elif isinstance(error,BadArgument):
        await ctx.send("Bad Argument")
    elif isinstance(error,MissingRequiredArgument):
        await ctx.send('Missing Required Argument')    
    else:
        print(f'Ignoring exception in command {ctx.command.name}', file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr) 
        
@client.command()
async def load(ctx, extension):
    client.load_extension(F'cogs.{extension}')   

     
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}') 
         

client.run('DISCORD_TOKEN')
