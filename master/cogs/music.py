import discord, os, importlib, time , sys, json
from discord.ext import commands
from utils import permissions, default
from discord import option


class Music(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.slash_command(description="Play a song")
    async def play(self, ctx, name: str):
        if not ctx.author.voice:
            await ctx.respond("You have to be in a vc to use this command")





def setup(bot:commands.Bot):
    bot.add_cog(Music(bot))