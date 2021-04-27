# STATUS = INCOMPLETE
# will add create tables function later

import discord
import sqlite3
import time
from discord.ext import commands

client = commands.Bot(command_prefix="?")

connection = sqlite3.connect('accounts.db')

cursor = connection.cursor()


@client.event
async def on_ready():
    cursor.execute("select * from stock")
    total = len(cursor.fetchall())
    stream = discord.Streaming(name="In Stock: {}".format(total), url="https://twitch.tv/wrlddd")
    print('------')
    print(client.user.name + "#" + client.user.discriminator)
    print('------')
    await client.change_presence(status=discord.Status.idle, activity=stream)

@client.command()
async def gen(ctx):
    cursor.execute("select * from hulu")
    zx = len(cursor.fetchall())
    cursor.execute("select * from nordvpn")
    ll = len(cursor.fetchall())
    cursor.execute("select * from stock")
    res = len(cursor.fetchall())
    embed = discord.Embed(title = "PV-Gen | In Stock: {}".format(res), description = """
    Hulu - {}
    NordVPN - {}
    """.format(zx, ll), color = 0x3eb489)
    await ctx.send(embed = embed)

@client.command()
async def args(ctx, arg1, arg2):
    await ctx.send('You sent "{}" and "{}"'.format(arg1, arg2))

@client.command()
async def restock(ctx):
    await client.change_presence(activity=discord.Streaming(name="restocking combo..", url="https://twitch.tv/restocking"))
    await ctx.send("Enter in Combolist")

    msg1 = await client.wait_for('message')
    response1 = (msg1.content)
    zz = (msg1.content.split())

    await ctx.send("What site is this combolist for? [hulu, nordvpn] `Note: MAKE SURE YOU DO NOT ENTER IN EXTRA ARGUMENTS`")
    
    msg2 = await client.wait_for('message')
    response2 = (msg2.content.lower())

    for x in zz:
        cursor.execute("INSERT INTO {} VALUES ({})".replace("{}", "'{}'").format(response2, x))
        cursor.execute("INSERT INTO {} VALUES ({})".replace("{}", "'{}'").format('stock', x))
        connection.commit()
    
    await ctx.send("Done.")
    cursor.execute("select * from stock")
    total = len(cursor.fetchall())
    await client.change_presence(activity=discord.Streaming(name="In Stock: {}".format(total), url="https://twitch.tv/wrlddd"))

client.run("token")
