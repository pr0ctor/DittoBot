'''
Created on Feb 13, 2018

@author: ryanforsyth
'''
import discord
from discord.ext import commands
import asyncio
import discord.emoji
import random

Client=discord.Client()
bot=commands.Bot(command_prefix="#", description="Preparing for the future")
ChoiceArray=("@Person 1","@Person 2") #Removed id's for safety reasons
LiArray=("<:frankli:364521319234142228>","<:cowboyli:375353209369395239>","<:firechiefli:384806021257756672>","<:fiestali:377158127650603017>","<:doctorli:378254324465401866>")

Miracle=(" cures cancer", " ends world hunger"," defies gravity"," saves kittens from trees"," doubles your salary"," cures the blind"," walks on water",
" enslaved humanity"," sold drugs to children"," voted for trump"," wa wa wa wa wa wa wa wa wa "," won the SuperBowl"," divided by zero", " saved the world",
" is more interesting than the most interesting man on earth (stay thirsty my friend)"," can see why kids love the taste of cinnamon toast crunch"," passed a li without reading book <:fiestali:377158127650603017>",
" is the future"," can beat Chuck Norris in a fight","taught Bob Ross to paint", " can pronounce Kawlee's name" )
@bot.event
async def on_ready():
    print("Logged in as "+bot.user.name)
    
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
  
@bot.command(pass_context=True)
async def helps(ctx):
    embed = discord.Embed(title="{}'s guide".format(bot.user.name), description="Help section", color=0x00ff00)
    embed.add_field(name="Cookie", value="{} begs for cookie (@bot to give cookie)".format(bot.user.name))
    embed.add_field(name="Dr.Li", value="Display li upon mention or ask li what's your grade")
    embed.add_field(name="Dr.Ai", value="Display Ai upon mention or ask Ai what's your grade")
    embed.add_field(name="Harper", value="Display Harper upon mention")
    embed.add_field(name="Zhong", value="Display Zhong upon mention")
    embed.add_field(name="Bitcoin", value="Li likes bitcoin like {} likes cookies".format(bot.user.name))
    await bot.say(embed=embed)
#checks message for cookie
@bot.event
async def on_message(message): 
    print(message.author.name+": "+message.content)
    UserID=message.author.id    #gets user id
    #Bot want cookie
    if "cookie" in message.content.lower() and message.author.id != bot.user.id and message.content!=("<@%s>\n{cookie}"%(UserID)):
       await bot.send_message(message.channel, "<@%s> Bot want cookie :sob:" % (UserID)) #prints message and tags user
    #Give a bot a cookie
    elif(message.content==("<@%s> \N{cookie}")%(bot.user.id)):
        await bot.send_message(message.channel,"<@%s> Thank you! :yum:"%(UserID))
    #Dr.Li
    elif(("dr. li" in message.content.lower() or ':frankli:' in message.content or ':firechiefli:' in message.content or 
    ':cowboyli:' in message.content or ':doctorli:' in message.content or ':fiestali:' in message.content )
    and message.author.id != bot.user.id):
        
        emoji=random.randint(0,4)
        output=LiArray[emoji]
        if( "what's my grade?" in message.content.lower() ):
            lowergrade=random.randint(0,50)
            uppergrade=random.randint(60,100)
            output=output+" NO CURVE! but your "+ str(lowergrade)+" is a"+str(uppergrade)+"\n"
        await bot.send_message(message.channel,output+" Just eh, read the book! ok...")
    
    #Dr.Ai
    elif(("dr. ai" in message.content.lower() or ':chunyuai:' in message.content) and message.author.id != bot.user.id):
        output="<:chunyuai:385232742121603073>"
        if( "what's my grade?" in message.content.lower() ):
            grade=random.randint(70,100)
            output=output+" In my class what, your grade is what "+str(grade)+"\n"
       
        await bot.send_message(message.channel,output+" what")
        
    #Harper
    elif(("harper" in message.content.lower() or ':ryanharper:' in message.content)and message.author.id != bot.user.id):
        await bot.send_message(message.channel," <:ryanharper:364591097944604672> <@Person3> you're fired!")#id removed for safety
    
    #Zhong
    elif (("zhong" in message.content.lower() or ':weizhong:' in message.content or "scalawa" in message.content.lower() or "scala" in message.content.lower())
    and message.author.id != bot.user.id): 
        emoji=random.randint(0,21)
        output="<:weizhong:385232792981602306> <:scalawa:390024837210439682> does wa, it" + Miracle[emoji]+"! wa"
        await bot.send_message(message.channel,output)
    #Li want bitcoin
    elif "bitcoin" in message.content.lower() and message.author.id != bot.user.id and "@li" not in message.content.lower():
        emoji=random.randint(0,4)
        output=LiArray[emoji]
        await bot.send_message(message.channel, "<@%s>"% (UserID)+ output +" want bitcoin :sob:") #prints message and tags user
    #Give a li a bitcoin
    elif( "@li" in message.content and ":bitcoin:" in message.content):
        emoji=random.randint(0,4)
        output=LiArray[emoji]
        await bot.send_message(message.channel,output+"<@%s> THE PRECIOUS! THE PRECIOUS! KSSSSSSSS"%(UserID))
    #bad bot
    elif("bad bot" in message.content.lower() or "bad <@%s>"%(bot.user.id) in message.content.lower()):
        await bot.send_message(message.channel,":sob: :cry:")
    #good bot
    elif("good bot" in message.content.lower() or "good <@%s>"%(bot.user.id) in message.content.lower()):
        await bot.send_message(message.channel,":smiley: :innocent:")
   #Help 
    elif("<@%s> help"%(bot.user.id) in message.content.lower()  and message.author.id != bot.user.id):
        await bot.send_message(message.channel,"Here to help!")
        message.content="#helps"
    #schwartz
    elif(("<:amandaschwartz:364514515502759937>" in message.content or "schwartz" in message.content.lower()) and message.author.id != bot.user.id   ):
        output="<:amandaschwartz:364514515502759937>" 
        if("where are you from?" in message.content.lower()):
            output=output+" (In Canadian accent) I am not Canadian, eh!"
        await bot.send_message(message.channel,output)
    #lewis
    elif("lewis" in message.content.lower() and message.author.id != bot.user.id):
        await bot.send_message(message.channel,"<:jeromelewis:411204652634472449> good day ladies and beasts")
    #Creepy
    elif("<:swirlds:413774365864362005>" in message.content and message.author.id != bot.user.id):
        victim=random.randint(0,1)
        victim=ChoiceArray[victim]
        await bot.send_message(message.channel,"<:swirlds:413774365864362005> ***WANNA SEE MY HASHGRAPH*** "+victim+ "***???*** <:swirlds:413774365864362005>" );
    await bot.process_commands(message)
bot.run(Key) #Insert key here