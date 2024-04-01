import discord, os, importlib, time , sys, json
from discord.ext import commands
from utils import permissions, default
from discord import option


class Manager(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.slash_command(description="Loads an extension")
    @commands.check(permissions.is_owner)
    async def load(self, ctx, name: str):

        try:
            self.bot.load_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.respond(default.traceback_maker(e))
        await ctx.respond(f"Loaded extension **{name}.py**")

    @commands.slash_command(description="Unloads an extension")
    @commands.check(permissions.is_owner)
    async def unload(self, ctx, name: str):
        try:
            self.bot.unload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.respond(default.traceback_maker(e))
        await ctx.respond(f"Unloaded extension **{name}.py**")

    @commands.slash_command(description="Reloads an extension")
    @commands.check(permissions.is_owner)
    async def reload(self, ctx, name: str):
        try:
            self.bot.reload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.respond(default.traceback_maker(e))
        await ctx.respond(f"Reloaded extension **{name}.py**")

    @commands.slash_command(description="Reloads all extension")
    @commands.check(permissions.is_owner)
    async def reloadall(self, ctx):
        error_collection = []
        for file in os.listdir("./master/cogs"):
            if file.endswith(".py"):
                name = file[:-3]
                try:
                    self.bot.reload_extension(f"cogs.{name}")
                except Exception as e:
                    error_collection.append(
                        [file, default.traceback_maker(e, advance=False)]
                    )

        if error_collection:
            output = "\n".join([f"**{g[0]}** ```diff\n- {g[1]}```" for g in error_collection])
            return await ctx.respond(
                f"Attempted to reload all extensions, was able to reload, "
                f"however the following failed...\n\n{output}"
            )

        await ctx.respond("Successfully reloaded all extensions")

    @commands.slash_command(description="Reloads a util [CAN CAUSE CRASHES]")
    @commands.check(permissions.is_owner)
    async def reloadutils(self, ctx, name: str):
        name_maker = f"utils/{name}.py"
        try:
            module_name = importlib.import_module(f"utils.{name}")
            importlib.reload(module_name)
        except ModuleNotFoundError:
            return await ctx.respond(f"Couldn't find module named **{name_maker}**")
        except Exception as e:
            error = default.traceback_maker(e)
            return await ctx.respond(f"Module **{name_maker}** returned error and was not reloaded...\n{error}")
        await ctx.respond(f"Reloaded module **{name_maker}**")




def setup(bot:commands.Bot):
    bot.add_cog(Manager(bot))