import discord
from discord.ext import commands
from discord import option

class UserInfo(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.slash_command(description="Get a user's info")
    @option("member", discord.Member, required=True)
    async def userinfo(self, ctx, member):

        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(color=0xFFFF00, description=member.mention)
        embed.set_author(name=str(member.name), icon_url=member.avatar.url)
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Joined", value=member.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name="Join position", value=str(members.index(member)+1))
        embed.add_field(name="Registered", value=member.created_at.strftime(date_format))
        if len(member.roles) > 1:
            role_string = ' '.join([r.mention for r in member.roles][1:])
            embed.add_field(name="Roles [{}]".format(len(member.roles)-1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])
        embed.add_field(name="Guild permissions", value=perm_string, inline=False)
        embed.set_footer(text='ID: ' + str(member.id))
        
        await ctx.respond(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(UserInfo(bot))