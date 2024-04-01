import discord, time
from discord.ext import commands
from utils import default
from datetime import datetime

config = default.config()

def generalLogger(action, responsible):

    embed = discord.Embed(title="General Logger", color = 0xFFFF00)
    embed.add_field(name="Action", value=action)
    embed.add_field(name="User Responsible", value=responsible)

    return embed

def channelActionLog(action, channel, arg):


    embed = discord.Embed(title="Channels Logs")
    embed.add_field(name="Channel Affected", value=channel)
    embed.add_field(name=action, value=arg)

    return embed

def moderatorActionLog(mod, user, reason, type):

     
    embed = discord.Embed(title=f'User {type}ed', color=0x008000)
    embed.add_field(name="Moderator Responsible", value=f"{mod} - {mod.id}", inline=False)
    embed.add_field(name="Target", value=f"{user} - {user.id}", inline=False)
    embed.add_field(name="Reason", value=reason)
    embed.timestamp = datetime.utcnow()

    return embed


def moderatorActionTimeoutLog(mod, user, reason, duration):

     
    embed = discord.Embed(title=f'User timed out for {duration}', color=0x008000)
    embed.add_field(name="Moderator Responsible", value=f"{mod} - {mod.id}", inline=False)
    embed.add_field(name="Target", value=f"{user} - {user.id}", inline=False)
    embed.add_field(name="Reason", value=reason)
    embed.timestamp = datetime.utcnow()

    return embed

def notifyUser(mod, reason, type):

    embed = discord.Embed(title=f"You have been {type}ed by {mod}")
    embed.add_field(name="Reason", value=f"{reason}")
    return embed

def notifCheck(check):

    if check == True:

        embed = discord.Embed(title=f"Member Informed of Mod Action", color = 0x00ff00)
        return embed
    
    else: 

        embed = discord.Embed(title=f"Something went wrong while informing the member of the mod action", color=0x008000)
        embed.add_field(name="Reason", value="Member has DMs closed or has blocked me!")

        return embed


def eventLogger(action, arg):
    embed = discord.Embed(title=f"{action}", description=f"{arg}" ,color=discord.Color.gold())
    return embed