import discord
from discord.ext import commands
from utils import logger, default

config = default.config()

class Logging(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.modlog = bot.get_channel(int(config["modlogChannel"]))

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages:list):
        log = logger.eventLogger("bulk_message_delete", messages)
        await self.modlog.send(log)
        
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel:discord.abc.GuildChannel):

        log = logger.eventLogger("guild_channel_create", channel)
        await self.modlog.send(log)

    
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel:discord.abc.GuildChannel):
        log = logger.eventLogger("guild_channel_delete", channel)
        await self.modlog.send(log)

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before:discord.abc.GuildChannel, after:discord.abc.GuildChannel):
        log = logger.eventLogger("guild_channel_update", [before, after])
        await self.modlog.send(log)
    
    @commands.Cog.listener()
    async def on_guild_integrations_update(self, guild:discord.Guild):

        log = logger.eventLogger("guild_integrations_update", guild)
        await self.modlog.send(log)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role:discord.Role):

        log = logger.eventLogger("guild_role_create", role)
        await self.modlog.send(log)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role:discord.Role):

        log = logger.eventLogger("guild_role_delete", role)
        await self.modlog.send(log)

    @commands.Cog.listener()
    async def on_guild_role_update(self, before:discord.Role, after:discord.Role):
        log = logger.eventLogger("guild_role_update", [before,after])
        await self.modlog.send(log)

    @commands.Cog.listener()
    async def on_message_delete(self, message:discord.Message):

        log = logger.eventLogger("message_delete", [message.author, message.content])
        await self.modlog.send(log)

    @commands.Cog.listener()
    async def on_message_edit(self, before:discord.Message, after:discord.Message):

        log = logger.eventLogger("message_edit", [before, after])
        await self.modlog.send(log)


def setup(bot:commands.Bot):
    bot.add_cog(Logging(bot))