# Testbot by EIjo & Jarifa

import discord
from discord.ext import commands

import cubify

bot = commands.Bot(command_prefix='#')
botTitle = "Testbot"
botVersion = "1.0"


@bot.event
async def on_ready():
    print("Bot starting...")
    print("Bot Version: " + botTitle + " " + botVersion)
    print("userid: " + bot.user.id)
    print("Startup complete.")


@bot.event
async def on_message(message):
    if message.content.startswith('#ping'):
        user_id = message.author.id
        await bot.send_message(message.channel, "<@%s> Pong!" % (user_id))

    if message.content.startswith('#cube'):
        content = message.content[6:]
        cubified = cubify.cubify(word=content, subsqaures=(0 == 0))
        if not cubified:
            await bot.send_message(message.channel,
                                   "Invalid text. \n"
                                   "try a world that starts and ends with the same letter\n"
                                   "The word also has to be at least 5 letters long")
        else:
            await bot.send_message(message.channel, "```\n" + cubified + "```")

    if message.content.startswith('#help'):
        embed = discord.Embed(title=botTitle + " version: " + botVersion, description="The list of commands are:")
        embed.add_field(name="#ping", value="returns 'Pong!'")
        embed.add_field(name="#cube", value="returns cubified version of input")

        await bot.send_message(message.channel, embed=embed)


try:
    with open("testfile.txt") as f:
        bot.run(f.read())
except Exception:
    print("Invalid token")
