import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Starting...")

@client.event
async def on_message(message):
    if message.content.startswith("봇아 안녕"):
        await message.channel.send("반가워!")

@client.event
async def on_message(message):
    if message.content.startswith("봇아 ㅎㅇ"):
        await message.channel.send("ㅎㅇ!")

@client.event
async def on_message(message):
    if message.content.startswith("안녕하세요"):
        await message.channel.send("안녕하세요!")

@client.event
async def on_message(message):
    if message.content.startswith("봇아 뭐해?"):
        await message.channel.send("아무것도 안하고 있어!")

@client.event
async def on_message(message):
    if message.content.startswith("봇아"):
        await message.channel.send("왜앵")

@client.event
async def on_message(message):
    if message.content.startswith("ㅅㅂ"):
        await message.channel.send("욕하지마")

@client.event
async def on_message(message):
    if message.content.startswith("ㅁㅊ"):
        await message.channel.send("욕하지마")

@client.event
async def on_message(message):
    if message.content.startswith("봇아 뭐할래?"):
        await message.channel.send("그러게...")                        

client.run("NzkzNjU0MDYzNzg2MzYwODQy.X-vZ8g.u8--Xg0eFsevnv9Y5le3FXknIPE")