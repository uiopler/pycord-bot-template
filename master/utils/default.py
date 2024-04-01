import json, discord, traceback, time, os ,sys
from pathlib import Path
from io import BytesIO
from datetime import datetime


def get_path():
    cwd = Path(__file__).parents[0]
    cwd = str(cwd)
    return cwd


def read_json(filename):
    cwd = get_path()
    with open(cwd + "/" + filename + ".json", "r") as file:
        data = json.load(file)
    return data


def write_json(data, filename):
    cwd = get_path()
    with open(cwd + "/" + filename + ".json", "w") as file:
        json.dump(data, file, indent=4)

def convert(time):

    pos = ["s", "m", "h", "d"]
    time_dict = {"s" : 1, "m": 60, "h": 3600, "d": 3600*24}
    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2
    return val * time_dict[unit]

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)


def config():
    # try:
        
        with open(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utils' ,'data', 'config.json')), encoding='utf8') as data:
            return json.load(data)
    # except FileNotFoundError:
    #     raise FileNotFoundError("JSON file wasn't found")


def change_config_value_int(value: str, to: int):
    config_name = (os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utils' ,'data', 'config.json')))
    with open(config_name, "r") as jsonFile:
        data = json.load(jsonFile)

    data[value] = to
    with open(config_name, "w") as jsonFile:
        json.dump(data, jsonFile, indent=2)


def change_config_value(value: str, to):
    config_name = (os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utils' ,'data', 'config.json')))
    with open(config_name, "r") as jsonFile:
        data = json.load(jsonFile)

    data[value] = to
    with open(config_name, "w") as jsonFile:
        json.dump(data, jsonFile, indent=2)

def traceback_maker(err, advance: bool = True):
    
    _traceback = ''.join(traceback.format_tb(err.__traceback__))
    error = ('```py\n{1}{0}: {2}\n```').format(type(err).__name__, _traceback, err)
    return error if advance else f"{type(err).__name__}: {err}"

def timetext(name):
    """ Timestamp, but in text form """
    return f"{name}_{int(time.time())}.txt"


def date(target, clock: bool = True, seconds: bool = False, ago: bool = False, only_ago: bool = False):
    if isinstance(target, int) or isinstance(target, float):
        target = datetime.utcfromtimestamp(target)

    unix = int(time.mktime(target.timetuple()))
    timestamp = f"<t:{unix}:{'f' if clock else 'D'}>"
    if ago:
        timestamp += f" (<t:{unix}:R>)"
    if only_ago:
        timestamp = f"<t:{unix}:R>"
    return timestamp


def responsible(target, reason):
    """ Default responsible maker targeted to find user in AuditLogs """
    responsible = f"[ {target} ]"
    if not reason:
        return f"{responsible} no reason given..."
    return f"{responsible} {reason}"


def actionmessage(case, mass=False):
    """ Default way to present action confirmation in chat """
    output = f"**{case}** the user"

    if mass:
        output = f"**{case}** the IDs/Users"

    return f"✅ Successfully {output}"


async def prettyResults(ctx, filename: str = "Results", resultmsg: str = "Here's the results:", loop=None):
    """ A prettier way to show loop results """
    if not loop:
        return await ctx.send("The result was empty...")

    pretty = "\r\n".join([f"[{str(num).zfill(2)}] {data}" for num, data in enumerate(loop, start=1)])

    if len(loop) < 15:
        return await ctx.send(f"{resultmsg}```ini\n{pretty}```")

    data = BytesIO(pretty.encode('utf-8'))
    await ctx.send(
        content=resultmsg,
        file=discord.File(data, filename=timetext(filename.title()))
    )

def modlog(member, action):
    embed = discord.Embed(title=f"{member.name}", description=f"{member.mention} has been {action}" ,color=discord.Color.gold())
    return embed

