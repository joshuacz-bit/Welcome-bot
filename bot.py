import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

WELCOME_CHANNEL_ID = 1456846567175622701

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel is None:
        return

    embed = discord.Embed(
        title="welcome 👋",
        description=f"yo {member.mention}, welcome to **{member.guild.name}**",
        color=discord.Color.green()
    )

    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
    embed.set_footer(text=f"member #{member.guild.member_count}")

    await channel.send(embed=embed)

bot.run(os.environ["DISCORD_TOKEN"])
