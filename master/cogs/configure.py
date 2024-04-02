import discord, json
from discord.ext import commands
from discord import option
from utils import permissions, default
from utils.default import config

config = config()


class Configure(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    # @commands.slash_command(description="Role Config")
    # @discord.default_permissions(administrator=True)
    # @option("key", description="what key would u like to edit", choices=["ticket_staff_role"])
    # @option("role", discord.Role, description="What role would you like to set")
    # async def configure_role(self, ctx, key, role):

    #     if key == "ticket_staff_role":
    #         default.change_config_value('ticketStaffRoleID', role.id)

    #         await ctx.respond(f"{role.mention} is now ticket staff role")

    #     else: 

    #         await ctx.respond(f"Something went wrong...")


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



    # @commands.slash_command(description="Toggle Automatic modules")
    # @discord.default_permissions(administrator=True)
    # @option("module", choices=["autorole", "automod"], required=True)
    # @option("type", choices=["On", "Off"], required=True)
    # async def toggle(self, ctx, module, type):

    #     if module == "autorole":

    #         if type == "On":

    #             default.change_config_value("autoroleEnabled", "True")
    #             await ctx.respond("Autorole has been Enabled")

    #         else:

    #             default.change_config_value("autoroleEnabled", "False")
    #             await ctx.respond("Autorole has been Disabled")

    #     elif module == "automod":

    #         if type == "On":
                
    #             default.change_config_value("automodEnabled", "True")
    #             await ctx.respond("Automod has been Enabled")
            
    #         else: 

    #             default.change_config_value("automodEnabled", "False")
    #             await ctx.respond("Automod has been Disabled")

def setup(bot:commands.Bot):
    bot.add_cog(Configure(bot))