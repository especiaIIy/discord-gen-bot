# STATUS: INCOMPLETE

import discord
import sqlite3
from discord.ext import commands

client = commands.Bot(command_prefix="?")

connection = sqlite3.connect('accounts.db')

cursor = connection.cursor()

numba = 0
total = 0

@client.event
async def on_ready():
    stream = discord.Streaming(name="best generator!!", url="https://twitch.tv/wrlddd")
    print('------')
    print(client.user.name + "#" + client.user.discriminator)
    print('------')
    await client.change_presence(status=discord.Status.idle, activity=stream)

@client.command()
async def gen(ctx):
    cursor.execute("select * from hulu")
    res = cursor.fetchall()
    numba = len(res)
    tt = total + numba
    embed = discord.Embed(title = "PV-Gen | In Stock: {}".format(tt), description = """
    Hulu - {}
    Spotify - 
    Buffalo Wild Wings - 
    NordVPN - 
    """.format(numba), color = 0x3eb489)
    await ctx.send(embed = embed)

@client.command()
async def args(ctx, arg1, arg2):
    await ctx.send('You sent "{}" and "{}"'.format(arg1, arg2))

@client.command()
async def restock(ctx):
    stream = discord.Streaming(name="restocking combo..", url="https://twitch.tv/restocking")
    await client.change_presence(activity=stream)
    await ctx.send("Enter in Combolist")

    msg1 = await client.wait_for('message')
    response1 = (msg1.content)
    zz = (msg1.content.split())
    v = len(zz)

    await ctx.send("What site is this combolist for? [hulu, netflix] `Note: MAKE SURE YOU DO NOT ENTER IN EXTRA ARGUMENTS`")
    
    msg2 = await client.wait_for('message')
    response2 = (msg2.content.lower())

    for x in zz:
        cursor.execute("INSERT INTO {} VALUES ({})".replace("{}", "'{}'").format(response2, x))
        connection.commit()
        stream2 = discord.Streaming(name="restocked", url="https://twitch.tv/restocked")
        await client.change_presence(activity=stream2)
    

client.run("token")
