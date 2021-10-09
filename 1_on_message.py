import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready")
    print("************")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content == 'hello':
        await msg.channel.send("Yo")

client.run('ODk1NDI1MDcyNDE4OTE4NTMx.YV4XlQ.YAbZijFXksSF4TkQQRyUlLRriwE')
