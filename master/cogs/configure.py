import discord, json
from discord.ext import commands
from discord import option
from utils import permissions, default
from utils.default import config

config = config()


class Configure(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot



    @commands.slash_command(description="Edits bot configs")
    @discord.default_permissions(administrator=True)
    @option("key", description="What key would you like to edit", choices=["none"])
    @option("channel", discord.TextChannel ,description="What channel would you like to set it")
    async def configure(self, ctx, key, channel):
        if key == "none":
            await ctx.respond("Not configured")

        else:    
            default.change_config_value(f"{key}Channel", channel.id)
            embed = discord.Embed(title=f"Set {key} channel to {channel.mention}", color=discord.Color.green())
            await ctx.respond(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(Configure(bot))