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

    if msg.content == 'cool':
        await msg.add_reaction('\U0001F60E')

@client.event
async def on_message_edit(before, after):
    await before.channel.send("--------------------")
    await before.channel.send(f'{before.author} edited a msg\n'
                              f'Before : {before.content}\n'
                              f'After : {after.content}')
    await before.channel.send("---------------------")

@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')

client.run('ODk1NDI1MDcyNDE4OTE4NTMx.YV4XlQ.YAbZijFXksSF4TkQQRyUlLRriwE')
