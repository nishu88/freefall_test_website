import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

a=0
b=0
c=0
ctr=0
l=[]
xd=0
t_end=0
fast=""

Client = discord.Client()
client = commands.Bot(command_prefix = "?")


@client.event
async def on_ready():
    print("Bot is online and connected to Discord")
##    await client.say("Bot is online and connected to Discord")
    await client.change_presence(game=discord.Game(name="Deciding what to PLAY"))


@client.event
async def on_message(message):
    
    
    global id1,a,b,c,ctr,l,xd,t_end,fast
    
    if message.content.lower() == "robot":
        await client.send_message(message.channel, ":robot:")        
        
    if message.content.lower() == "owner" or message.content.lower() == "?father" or message.content.lower() == "?owner" or message.content.lower() == "?maker":
        await client.send_message(message.channel, "<@277695189131460609> NISHANTH D A")

    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))

    if message.content.lower() == "?here":          
        if str(message.author.id)=="277695189131460609" :
            id1= str(message.channel.id )
            #await client.send_message(message.channel, "Listening to <#%s>" % (message.channel.id))
    
         
    if message.content.lower().startswith('1') or message.content.lower().startswith('2') or message.content.lower().startswith('3') and str(message.channel.id)==id1:
        
        if xd==0:
            t_end=time.time()+12
            xd=1
        
        while time.time() < t_end:
            print(t_end)
            print(time.time())
            
            if ctr <3:
                l.append(message.author.name)
                if(len(l)>2):
                    for i in l:
                        fast= fast + str(i) +"\n"
                        print(fast)
                    
                f1=open("fastest.txt",'w', encoding="utf-8")
                f1.write(str(fast))
                f1.close()
            ctr=ctr+1                    
                

            if message.content.lower().startswith('1'):
                if str(message.channel.id)==id1 :            
                    a=a+1
                    await client.send_message(discord.Object(id="478607577366921283"), "Option 1= "+str(a)+"\n"+"Option 2= "+str(b)+"\n"+"Option 3= "+str(c))
            if message.content.lower().startswith('2'):
                if str(message.channel.id)==id1 :
                    b=b+1
                    await client.send_message(discord.Object(id="478607577366921283"),"Option 1= "+str(a)+"\n"+"Option 2= "+str(b)+"\n"+"Option 3= "+str(c))
            if message.content.lower().startswith('3'):
                if str(message.channel.id)==id1 :
                    c=c+1
                    await client.send_message(discord.Object(id="478607577366921283"), "Option 1= "+str(a)+"\n"+"Option 2= "+str(b)+"\n"+"Option 3= "+str(c))
            
            while(True):        
                await asyncio.sleep(0.2)
                f = open("stats.txt", "w")
                f.write(str(a)+"\n"+str(b)+"\n"+str(c)+"\n")
                f.close()
        
        print(a,b,c)
        print(l)
        a=0
        b=0
        c=0
        f=open("stats.txt",'w')
        f.write("waiting for question")
        f.close()
        f1=open("fastest.txt",'w')
        f1.write("Name 1"+"\n"+"Name 2"+"\n"+"Name 3"+"\n")
        f1.close()        
        ctr=0
        xd=0
        fast=""
        l=[]


#client.run(os.getenv('TOKEN'))
client.run("NDc4NjEyMTE1MzYwNDQ4NTEz.DldVkQ._UOfgBuLjqD6_q-pAZaTmoAzmRw")







            
