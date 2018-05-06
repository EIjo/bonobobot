# Testbot by EIjo & Jarifa

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = discord.Client()
bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print("Test hehe xd")
    print("Bot Version: ")
    print("userid: "+bot.user.id)

@bot.event
async def on_message(message):
    if message.content.startswith('#ping'):
        userID = message.author.id
        await bot.send_message(message.channel, "<@%s> Pong!" % (userID))

    if message.content.startswith('#cube'):
        content = message.content[6:]
        cubified = "placeholder"
        await bot.send_message(message.channel, "```"+cubified+"```")

bot.run("NDQyNzg1NTg2NDAzNjA2NTU5.DdD7SA.7vDn92RKl0pVOczdCNrcelD2mD0")
