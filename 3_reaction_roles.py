import discord

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 896089397219450891

    async def on_ready(self):
        print('Bot is ready')
        print('************')

    async def on_raw_reaction_add(self, payload):
        if payload.message_id != self.target_message_id:
            return
        guild = client.get_guild(payload.guild_id)
        if payload.emoji.name == '🔴':
            role = discord.utils.get(guild.roles, name='Red')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🔵':
            role = discord.utils.get(guild.roles, name='Blue')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🟢':
            role = discord.utils.get(guild.roles, name='Green')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🟡':
            role = discord.utils.get(guild.roles, name='Yellow')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        if payload.message_id != self.target_message_id:
            return
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '🔴':
            role = discord.utils.get(guild.roles, name='Red')
            await member.remove_roles(role)
        elif payload.emoji.name == '🔵':
            role = discord.utils.get(guild.roles, name='Blue')
            await member.remove_roles(role)
        elif payload.emoji.name == '🟢':
            role = discord.utils.get(guild.roles, name='Green')
            await member.remove_roles(role)
        elif payload.emoji.name == '🟡':
            role = discord.utils.get(guild.roles, name='Yellow')
            await member.remove_roles(role)

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)

client.run('ODk1NDI1MDcyNDE4OTE4NTMx.YV4XlQ.YAbZijFXksSF4TkQQRyUlLRriwE')