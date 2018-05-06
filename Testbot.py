# Testbot by EIjo & Jarifa

import discord
import cubify
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = discord.Client()
bot = commands.Bot(command_prefix='#')
botTitle = "Testbot"
botVersion = "1.0"


@bot.event
async def on_ready():
    print("moker")
    print("Bot Version: "+botTitle+" "+botVersion)
    print("userid: " + bot.user.id)
    print("Startup complete.")

@bot.event
async def on_message(message):
    if message.content.startswith('#ping'):
        userID = message.author.id
        await bot.send_message(message.channel, "<@%s> Pong!" % (userID))

    if message.content.startswith('#cube'):
        content = message.content[6:]
        cubified = cubify.cubify(word=content, subsqaures=(0 == 0))
        if not cubified:
            await bot.send_message(message.channel, "invalid text try a world with at least 5 letters and with the same letter at the beginning as the end")
        else :
            await bot.send_message(message.channel, "```\n" + cubified + "```")

    if message.content.startswith('#help'):
        embed = discord.Embed(title=botTitle + " version: " + botVersion, description="The list of commands are:")
        embed.add_field(name="#ping", value="returns 'Pong!'")
        embed.add_field(name="#cube", value="returns cubified version of input")

        await bot.send_message(message.channel, embed=embed)


bot.run(input("Input bot token: "))
# Testbot by EIjo & Jarifa

import discord
import cubify
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = discord.Client()
bot = commands.Bot(command_prefix='#')
botTitle = "Testbot"
botVersion = "1.0"


@bot.event
async def on_ready():
    print("Bot starting...")
    print("Bot Version: "+botTitle+" "+botVersion)
    print("userid: " + bot.user.id)
    print("Startup complete.")

@bot.event
async def on_message(message):
    if message.content.startswith('#ping'):
        userID = message.author.id
        await bot.send_message(message.channel, "<@%s> Pong!" % (userID))

    if message.content.startswith('#cube'):
        content = message.content[6:]
        cubified = cubify.cubify(word=content, subsqaures=(0 == 0))
        await bot.send_message(message.channel, "```\n" + cubified + "```")

    if message.content.startswith('#help'):
        embed = discord.Embed(title=botTitle + " version: " + botVersion, description="The list of commands are:")
        embed.add_field(name="#ping", value="returns 'Pong!'")
        embed.add_field(name="#cube", value="returns cubified version of input")

        await bot.send_message(message.channel, embed=embed)


bot.run(input("Input bot token: "))
