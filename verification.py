## TODO: VERIFICATION
import discord
from discord.ext import commands

TOKEN = ""

client = commands.Bot(command_prefix =".")

@client.event
async def on_ready():
    print("Der Bot ist nun Online!")
    await client.change_presence(activity=discord.Game(name='verification'))

@client.event
async def on_message(message):
    print("{}".format(message.author.mention) + " " +  message.content)
    await client.process_commands(message)


@client.command()
async def accept(ctx):
    print("lol")
    print(ctx.message.channel.id)
    if ctx.message.channel.id == 588639741688283137:
        await ctx.author.send("**You accepted the testserver's rules**")
        roles = ctx.message.guild.roles
        for role in roles:
            if(role.name == "Member"):
                await ctx.message.author.add_roles(role, reason="Member accepted the rules.")

client.run(TOKEN)
