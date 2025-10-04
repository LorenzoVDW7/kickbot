from discord.ext import commands
import discord
import logging
from config import token as client_token

handler = logging.FileHandler(filename='kickbot.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def preview(ctx, description='Shows a preview of users that would be kicked by the "/Kick" command'):
    lurker_role = discord.utils.get(ctx.guild.roles, name='Lurker')
    usernames = [member.name for member in ctx.guild.members if lurker_role in member.roles]
    await ctx.send(usernames)

bot.run(client_token)



