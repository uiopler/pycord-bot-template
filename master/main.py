import discord, os
from discord.ext import commands
from win10toast import ToastNotifier as toast
from colorama import Fore as f
from utils import default, permissions, logger
from discord import option
from utils import permissions
from dotenv import load_dotenv
load_dotenv("env.env")
token = (str(os.getenv("TOKEN")))


config = default.config()

class Initializer(discord.Bot):
    def __init__(self):
        super().__init__(
            intents = discord.Intents.all(),
            case_insensitive = True
        )
        self.persistent_views_added = False
    
    async def on_ready(self):
        # if not self.persistent_views_added:
        #     self.add_view((view()))

        
        toast_notifier = toast()
        toast_notifier.show_toast(f"{config["name"]}", "Bot is now Running!", duration=2)
        print(f'{f.GREEN}Running Version: {f.YELLOW} {config["version"]} {f.RESET}')

bot = Initializer()

@bot.slash_command(description="Reloads the bot configuration")
@commands.check(permissions.is_owner)
async def restart(ctx):

    try:   
        await ctx.respond("Restarting...")
        default.restart_bot()

    except Exception as e:

        embed = discord.Embed(title="Something went wrong while reloading the bot", description=f"{e}", color=0xFF0000)
        await ctx.respond(embed=embed)

    
@bot.slash_command()
async def version(ctx):
    await ctx.respond(config['version'])

try:
    extensions = ['cogs.configure','cogs.manager','cogs.userinfo', 'cogs.ring']
    try:
        for i in extensions:
            bot.load_extension(i)
            print(f'{f.MAGENTA} + {f.RESET} {f.GREEN} LOADED {f.MAGENTA} {i} {f.RESET}')

    except Exception as e:

        print(e)

    bot.run("MTIwMjcwMzYzMTc5MTQzMTcwMA.G8sQod.k6hrMdPXN5uEnRqVwoJAcyApWuNsvouCz_mOIg")
    

except Exception as e:
    print(e)
