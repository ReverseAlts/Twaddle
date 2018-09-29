import discord
from discord.ext.commands import Bot
from discord.ext import commands
import json
import os
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()
os.chdir(r'C:\Users\twoby\Desktop\Bot')


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='On Twaddler'))
    print('Ready') 


@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    with open('users.json', 'w') as f:
        json.dump(users, f)

        
@client.event
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)

    with open('users.json', 'w') as f:
        json.dump(users, f)


async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['experience'] = 0
        users[user.id]['level'] = 1

async def add_experience(users, user, exp):
    users[user.id]['experience'] += exp
    

async def level_up(users, user, channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await client.send_message(channel, '{} has leveled up to level {}'.format(user.mention, lvl_end))
        users[user.id]['level'] = lvl_end




@client.event
async def on_message(message):
    if message.content == '!purchase':
        await client.send_message(message.channel,'https://selly.gg/p/804dbb2c')
    if message.content == '!duck':
        em = discord.Embed(description='Keep On Twaddling')
        em.set_image(url='')
        await client.send_message(message.channel, embed=em)
    if ('Hacking') in message.content:
       await client.delete_message(message)
    if ('Cheating') in message.content:
       await client.delete_message(message)
    if ('Banned') in message.content:
       await client.delete_message(message)
    if ('Ban') in message.content:
       await client.delete_message(message)
    if ('Gay') in message.content:
       await client.delete_message(message)
    if ('Homo') in message.content:
       await client.delete_message(message)
    if ('Muslims') in message.content:
       await client.delete_message(message)
    if ('Fuck') in message.content:
       await client.delete_message(message)
    if ('Shit') in message.content:
       await client.delete_message(message)
    if ('ArseHole') in message.content:
       await client.delete_message(message)
    if ('Nigger') in message.content:
       await client.delete_message(message)
    if ('Nigga') in message.content:
       await client.delete_message(message)
    if ('Bitch') in message.content:
       await client.delete_message(message)
    if ('dick') in message.content:
       await client.delete_message(message)
    if ('cock') in message.content:
       await client.delete_message(message)
    if message.content.startswith('!fact'):
        randomlist = ['Reverse Alts Is Named After The Reverse Hacked Client!','ZachSOnline is gay','Nocti is a Reverse Dev','Twaddler is an inside a joke','The developer of Minecraft is here','ZachSOnline has hacked since 2017','It took all night to make me','VPN stands for virtual private network','Hypixel relies so heavily on Watchdog that if it didnt exist Hypixel would get overun with hackers','ZachSOnline is called Zach']
        await client.send_message(message.channel,(random.choice(randomlist)))


    
client.run('NDk1NjUzNTc2ODYyMDcyODMy.DpFNTw.QsemN5jOortsizIHoAcvYUfVFOk')
