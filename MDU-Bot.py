#imports
import discord
import math
import youtube_dl
from youtube_dl import YoutubeDL
from discord.ext import commands
import discord.utils
from discord.utils import get as get


#variable initialization and declaration
client = discord.Client()
token = ". . ."
command = "$"

tiers = ["1E", "1D", "1C", "1B", "1A", "2D", "2C", "2B", "2A", "3D", "3C", "3B", "3A",
"4C", "4B", "4A", "5C", "5C+", "5B-", "5B", "5B+", "5A", "5A+"]

queue = []  #queue will store a list of songs

async def playSong(ctx, song):
    ydl_opts = {'format': 'bestaudio'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(song, download=False)
    URL = info['formats'][0]['url']
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegOpusAudio(source=URL), after=lambda e: print('done', e))
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #Simple bot test, will edit later for cleaner code//implement queues
    if message.content.startswith(command + "play"):
        messageSplit = message.content.rsplit(" ")
        if messageSplit[1].startswith("https://www.youtube.com/watch?v="):
            song = messageSplit[1]
            channel = message.author.voice.channel
            await channel.connect()
            await playSong(channel, song)
            await message.channel.send("Now playing... " + messageSplit[1] + ". In channel: " + str(channel))
        else:
            await message.channel.send("URL Error. Please enter a valid Youtube link. (\"https://www.youtube.com/watch?v=\")")



    if message.content.startswith(command + "tiers"):
        await message.channel.send('```Tier|| Numbers' 
            "\n1E  || 1"
            "\n1D  || 2"
            "\n1C  || 3"
            "\n1B  || 4"
            "\n1A  || 5"
            "\n2D  || 6"
            "\n2C  || 7"
            "\n2B  || 8"
            "\n2A  || 9"
            "\n3D  || 10"
            "\n3C  || 11"
            "\n3B  || 12"
            "\n3A  || 13"
            "\n4C  || 14"
            "\n4B  || 15"
            "\n4A  || 16"
            "\n5C  || 17"
            "\n5C+ || 18"
            "\n5B- || 19"
            "\n5B  || 20"
            "\n5B+ || 21"
            "\n5A  || 22"
            "\n5A+ || 23"
            "```"
            )

    if message.content.startswith(command + "cspeed"):
        thisthat = message.content.rsplit(" ")
        unpowSpeed = tiers.index(thisthat[2])
        powSpeed = tiers.index(thisthat[1])
        temporaryVar = math.floor((powSpeed - unpowSpeed)/2)
        newVar = unpowSpeed + temporaryVar
        combSpeed = tiers[int(newVar)+1]
        await message.channel.send("your combat speed is " + combSpeed)


client.run(token)
