import uuid
from discord.ext import commands
import discord


@client.command()
@commands.has_role("Admin")
async def gen(ctx,):
 key = str(uuid.uuid4())
 print(type(key))
 await ctx.reply(f"Here Is Your Generated Key - ``{key}``")
 with open("keys.txt", "a") as f:
   f.write(key  + "\n")




@client.command()
async def claim(ctx, key,):
 keys = open('keys.txt', 'r')
 read_content = keys.read()
 if f"{key}" in read_content:
    await ctx.reply('Key Valid Enjoy!')
    member = ctx.message.author
    guilds = ctx.guild
    role = discord.utils.get(ctx.guild.roles, name="Buyer")
    await member.add_roles(role)
    with open("keys.txt", "r") as f:
     lines = f.readlines()

    with open("keys.txt", "w") as f:
     for line in lines:
        if line.strip("\n") != key:
            f.write(line)
 else:
    await ctx.reply('Invalid!')
