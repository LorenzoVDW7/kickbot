import discord
from discord.ext import commands
from discord import app_commands
import logging
from config import token as client_token, server_id

class Client(commands.Bot):
    async def on_ready(self):
        guild = discord.Object(id=server_id)

        print(f'Logged in as {self.user}')

        try:
            synced = await self.tree.sync(guild=guild)
            print(f"synced {len(synced)} commands to guild {guild.id}")

        except Exception as e:
            print(f"Error syncing commands to guild {guild.id}: {e}")
            pass


handler = logging.FileHandler(filename='kickbot.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
GUILD_ID = discord.Object(id=server_id)

client = Client(command_prefix="!", intents=intents)

def get_roles(context):
    return [roles for roles in context.guild.roles]


@client.tree.command(name="preview", description='Preview the members that the "/Kick" command would remove',
                  guild=GUILD_ID)
async def show_preview(interaction: discord.Interaction, role: str):
    await interaction.response.send_message(role)


client.run(client_token)



