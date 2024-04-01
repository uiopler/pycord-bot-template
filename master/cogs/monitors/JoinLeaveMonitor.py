import discord, aiohttp, io
from discord.ext import commands
from utils.default import config

config = config()

class JoinLeaveMonitor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):
        
        async with aiohttp.ClientSession() as WelSession:
            async with WelSession.get(f'https://some-random-api.com/welcome/img/6/stars?type=join&username={member.name}&avatar={member.display_avatar.with_static_format("png").url}&memberCount=0&guildName={config["guildName"]}&textcolor=white&key=qpAR7udYPPFDMiYbkhxEeLNlY&font=1') as welImg:
                imageData = io.BytesIO(await welImg.read()) 
                
                channel =  self.bot.get_channel(int(config['welcomeChannel']))
                await channel.send(file=discord.File(imageData, 'welcome.png'))

                await WelSession.close()
        
    @commands.Cog.listener()
    async def on_member_remove(self, member):
            
        async with aiohttp.ClientSession() as LeaveSession:
            async with LeaveSession.get(f'https://some-random-api.com/welcome/img/1/stars?type=leave&username={member.name}&avatar={member.display_avatar.with_static_format("png").url}&memberCount=0&guildName={config["guildName"]}&textcolor=red&key=qpAR7udYPPFDMiYbkhxEeLNlY&font=1') as leaveImg:
                imageData = io.BytesIO(await leaveImg.read()) 
                
                channel = self.bot.get_channel(int(config["leaveChannel"]))
                await channel.send(file=discord.File(imageData, 'leave.png'))

                await LeaveSession.close()


def setup(bot):
    bot.add_cog(JoinLeaveMonitor(bot))