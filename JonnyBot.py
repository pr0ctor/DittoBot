'''
Created on Feb 13, 2018

@author: ryanforsyth
'''
import discord
from discord.ext import commands
import asyncio
import discord.emoji
from os import path

Client = discord.Client()
bot = commands.Bot(command_prefix="\\", description="Preparing for the future")

@bot.event
async def on_ready():
    print("Logged in as " + bot.user.name)

@bot.command(pass_context=True)
async def timeout(ctx,user: discord.Member):
    jonnyrole = discord.utils.get(ctx.message.server.roles,name='Jonny')

    await bot.replace_roles(user,jonnyrole)
    print("Gave "+ user.name+" a timeout.")

    jonnychannel = discord.utils.get(ctx.message.server.channels, name="Jonny's Timeout Corner", type=discord.ChannelType.voice)
    await bot.move_member(user, jonnychannel)
    print("Moved " + user.name + " to a timeout corner.")

    await bot.say("Done.")

@bot.command(pass_context=True)
async def free(ctx,user: discord.Member):
    guildmember = discord.utils.get(ctx.message.server.roles,name='Guild Members')

    await bot.replace_roles(user,guildmember)
    print("Gave " + user.name + " Freedom from the timeout.")

    general = discord.utils.get(ctx.message.server.channels, name="General", type=discord.ChannelType.voice)
    await bot.move_member(user,general)
    print("Moved " + user.name + " to General Chat")
    
    await bot.say("Done.")

@bot.command(pass_context=True)
async def helps(ctx):
    embed = discord.Embed(title="{}'s guide".format(bot.user.name), description="Help section", color=0x00ff00)
    embed.add_field(name="Timeout + @user", value="Demote user to Jonny Rank and move them to the Timeout Corner.")
    embed.add_field(name="Free + @user", value="Frees user from timeout and makes them a Guild Member again. Moves them to General.")
    embed.add_field(name="Help", value="Displays this message.")
    await bot.say(embed=embed)


# checks message for cookie
@bot.event
async def on_message(message):
    print(message.author.name + ": " + message.content)
    UserID = message.author.id  # gets user id
    await bot.process_commands(message)

if path.isfile("token.txt"):
    with open("token.txt") as f:
        token = f.readline()
    print("[INFO] Starting up and logging in...")
    bot.run(token)
else:
    print("Token not found.")

# bot.run(Key)  # Insert key here
