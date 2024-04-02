import discord, asyncio
from discord.ext import commands
from discord import option

class Ring(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.slash_command(description="Ring a user in a discord server")
    @option("member", discord.Member, required=True)
    async def ring(self, ctx, member):
        voice_state = ctx.author.voice

        if voice_state is None:
            return await ctx.respond('You need to be in a voice channel to ring someone')
        
        else:
            await ctx.respond(f"Trying to 'ring' {member.mention}")
            await member.send(f'{ctx.author.mention} is inviting you to join {ctx.author.voice.channel.mention}')
            await asyncio.sleep(1)
            await member.send(f"Ring, {ctx.author.voice.channel.mention}")
            await asyncio.sleep(1)
            await member.send(f"Rong, {ctx.author.voice.channel.mention}")
            await asyncio.sleep(1)
            await member.send(f"Bing, {ctx.author.voice.channel.mention}")
            await asyncio.sleep(1)
            await member.send(f"Bong, {ctx.author.voice.channel.mention}")
            await asyncio.sleep(1)
            await member.send("https://tenor.com/view/breaking-bad-walter-white-ringing-doorbell-gif-26055762")

            await ctx.send(f"I successfully rang {member.mention} (I spammed his dms)")


def setup(bot:commands.Bot):
    bot.add_cog(Ring(bot))