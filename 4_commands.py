from discord.ext import commands

bot = commands.Bot(command_prefix='-')

@bot.command()
async def punch(ctx, arg1):
    await ctx.send(f'Punched {arg1}')

@bot.command()
async def slap(ctx, arg1, arg2):
    await ctx.send(f'Slapped {arg1} and {arg2}')

@bot.command()
async def smack(ctx, *args):
    e = ', '.join(args)
    await ctx.send(f'Smacked {e}')

@bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

bot.run('ODk1NDI1MDcyNDE4OTE4NTMx.YV4XlQ.YAbZijFXksSF4TkQQRyUlLRriwE')

