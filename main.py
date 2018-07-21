import discord
import random
import time
from discord.ext import commands

myColor = 0x37B067
myVersion = "0.1.0"

token = "NDY2NDI0ODU0OTU0OTAxNTI0.DjDvUQ.UsrgeOHOowyOOf7vSi-Up-K18KQ"
client = commands.Bot(command_prefix=["()", "data."])
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Data will ()help you!", url="https://www.twitch.tv/data_the_bot", type=1))
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)

@client.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(title="", description="", color=myColor)
    embed.add_field(name="Utility", value="Type `()helpUtility` or `data.helpUtility` for more info.", inline=False)
    embed.add_field(name="Learn Coding", value="Type `()helpLearnCoding` or `data.helpUtility` for more info.", inline=False)
    embed.add_field(name="Fun", value="Type `()helpFun` or `data.helpFun` for more info.", inline=False)
    embed.add_field(name="Math", value="Type `()helpMath` or `data.helpMath` for more info.", inline=False)
    embed.add_field(name="Moderation", value="`Type ()helpModeration` or `data.helpModeration` for more info.", inline=False)
    embed.set_footer(text="Prefix : () & data.")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def helpUtility(ctx):
    embed=discord.Embed(title="", description="", color=myColor)
    embed.add_field(name="()ping", value="Returns pong, ping that pong!", inline=False)
    embed.add_field(name="()help", value="This nifty command!", inline=False)
    embed.add_field(name="()support", value="Returns the support server for me.", inline=False)
    embed.add_field(name="()invite", value="Returns the link to invite me.", inline=False)
    embed.add_field(name="()donate", value="Returns the link to donate to me.", inline=False)
    embed.add_field(name="()upvote", value="Upvote on Discord bot list.", inline=False)
    embed.add_field(name="()botinfo", value="I wonder what this does...", inline=False)
    embed.add_field(name="()serverinfo", value="Data digs up some info about the server.", inline=False)
    embed.set_footer(text="Prefix : () & data.")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def helpLearnCoding(ctx):
    embed=discord.Embed(title="", description="", color=myColor)
    embed.add_field(name="()learnPython", value="Returns a link to a Python tutorial.", inline=False)
    embed.add_field(name="()learnJava", value="Returns a link to a Java tutorial..", inline=False)
    embed.add_field(name="()learnJavaScript", value="Returns a link to a JavaScript tutorial.", inline=False)
    embed.add_field(name="()learnNodejs", value="Returns a link to a Node.js tutorial.", inline=False)
    embed.add_field(name="()learnHTML", value="Returns a link to a HTML tutorial.", inline=False)
    embed.add_field(name="Learn Discord libraries", value="Type `()helpLearnDiscordLibs` or `data.helpLearnDiscordLibs`for more info!", inline=False)
    embed.set_footer(text="Prefix : () & data.")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def helpFun(ctx):
    embed=discord.Embed(title="", description="", color=myColor)
    embed.add_field(name="()hello", value="You know this.", inline=False)
    embed.add_field(name="()8ball <question>", value="Ask the magical Data 8ball something. Don't expect something always to be nice...", inline=False)
    embed.add_field(name="()dice", value="Roll the dice.", inline=False)
    embed.add_field(name="()coin", value="Flip the coin.", inline=False)
    embed.add_field(name="()fidgetspinner", value="The almight fidget spinner will tell you your luck.", inline=False)
    embed.add_field(name="()say <content>", value="Data returns what you want it to.", inline=False)
    embed.add_field(name="()choose <option> <option>", value="Data chooses for when you want to settle the score some other way.", inline=False)
    embed.set_footer(text="Prefix : () & data.")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def helpLearnDiscordLibs(ctx):
    embed=discord.Embed(title="", description="", color=myColor)
    embed.add_field(name="()learnDiscordjs", value="Returns a brief explanation of how to install and where to learn Discord.js.", inline=False)
    embed.add_field(name="()learnDiscordpy", value="Returns a brief explanation of how to install and where to learn Discord.py.", inline=False)
    embed.add_field(name="Secret", value="Shhhhhhhhhhh. Your not supposed to know about `()helpSecret`!!")
    embed.set_footer(text="Prefix : () & data.")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def helpSecret(ctx):
    embed=discord.Embed(title="", description="", color=myColor)
    embed.add_field(name="()begoned", value="The right way of banning someone.", inline=False)
    embed.add_field(name="()kiiick", value="The ultamite soccer kick.", inline=False)
    embed.add_field(name="()randomemoji", value="Posts some random emoji.", inline=False)
    embed.add_field(name="()workonlist", value="Returns a list of ultamite commands that will be worked on in the near future!", inline=False)
    embed.set_footer(text="Don't tell anyone!")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def helpMath(ctx):
    embed=discord.Embed(title="", description="", color=myColor)
    embed.add_field(name="()add <int> <int>", value="Adds two numbers together.", inline=False)
    embed.add_field(name="()subtract <int> <int>", value="Subtracts two numbers.", inline=False)
    embed.add_field(name="()multiply <int> <int>", value="Multiplies two numbers together.", inline=False)
    embed.add_field(name="()divide <int> <int>", value="Divides two numbers together.", inline=False)
    embed.set_footer(text="Prefix : () & data.")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def helpModeration(ctx):
    embed=discord.Embed(title="", description="", color=myColor)
    embed.add_field(name="()kick <member>", value="Kicks a member from a server. Must have proper permissions to kick members.", inline=False)
    embed.add_field(name="()ban <member>", value="Lays the ban hammer upon thy member!. Must have proper permissions to ban members.", inline=False)
    embed.add_field(name="()clear <int>", value="Deletes a number of mesages.", inline=False)
    embed.set_footer(text="Prefix : () & data.")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def randomemoji(ctx):
    emojiList = [":grinning:", ":grimacing:", ":grin:", ":joy:", ":smile:", ":sweat_smile:", ":satisfied:", ":innocent:", ":wink:", ":blush:", ":slight_smile:", ":upside_down:", ":relaxed:"]
    emojiSelect = random.choice(emojiList)
    answer = ((emojiSelect))
    embed=discord.Embed(title=answer, description="", color=myColor)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def kiiick(ctx, userName: discord.User):
    author = ctx.message.author
    if author.server_permissions.kick_members == True:
        await client.kick(userName)
        embed = discord.Embed(title="GOOOOOOOOOOOOOOOOOOOOOAAAAAAAAAAAAAAAAAAAAAL!!", color=myColor)
        await client.say(embed=embed)
    if author.server_permissions.kick_members == False:
        permission_error = "You can't! REEEEEEEEE!"
        embed = discord.Embed(title=permission_error, color=myColor)
        await client.say(embed=embed)
    author = ctx.message.author

@client.command(pass_context=True)
async def begoned(ctx, userName: discord.User):
    author = ctx.message.author
    if author.server_permissions.ban_members == True:
        await client.ban(userName)
        embed = discord.Embed(title="BE GONE DEMON!", color=myColor)
        await client.say(embed=embed)
    if author.server_permissions.ban_members == False:
        permission_error = "You Can't! REEEEEEEEEE!"
        embed = discord.Embed(title=permission_error, color=myColor)
        await client.say(embed=embed)
    author = ctx.message.author

@client.command(pass_context=True)
async def workonlist(ctx):
    embed=discord.Embed(title="", description="", color=myColor)
    embed.add_field(name="Economy Commands", value="To bring a little light into people's lives. And cause leveling up is cool.", inline=True)
    embed.add_field(name="More Secret Commands", value="Because secret...", inline=False)
    embed.add_field(name="More Fun Commands", value="Because fun is part of this bot.", inline=False)
    await client.say(embed=embed)

@client.command(pass_context=True, name="8ball")
async def _8ball(ctx, *, arg):
    luckyList = ["No.", "Yes.", "Most likely.", "Not likely.", "Probably.", "Sure.", "Yea, I think you need a doctor.", "Ask BugHunter. kthx.", "No u.", "If you can read this, you can read.", "Why do you question me?!!"]
    luckySelect = random.choice(luckyList)
    answer = ((luckySelect) + " :8ball:")
    embed=discord.Embed(title=answer, description="", color=myColor)
    embed.set_footer(text="Question: " + arg)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def fidgetspinner(ctx):
    spinnerList = ["Your luck is bad, the fidget spinner is not in your favor!", "The fidget spinner is in your favor! Expect good luck!", "The fidget spinner does not know your future... Stay cautious!"]
    spinnerSelect = random.choice(spinnerList)
    answer = ((spinnerSelect) +" ߷")
    embed=discord.Embed(title=answer, description="", color=myColor)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(title="{}'s info".format(ctx.message.server.name), description="Here is what I could dig up from my inside sources...", color=myColor)
    embed.add_field(name="Name", value=ctx.message.server.name)
    embed.add_field(name="Server ID", value="`{}`".format(ctx.message.server.id))
    embed.add_field(name="Members", value="{}".format(len(ctx.message.server.members)))
    embed.add_field(name="Roles", value='{}'.format(len(ctx.message.server.roles)))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)

@client.command(pass_context=True, name="coin")
async def coin(ctx):
    coinList = ["Heads :white_circle: ", "Tails :black_circle:"]
    coinSelect = random.choice(coinList)
    answer = ((coinSelect))
    embed=discord.Embed(title=answer, description="", color=myColor)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def say(ctx, *args : str):
    output = ""
    for word in args:
        output = output + " " + word
    embed=discord.Embed(title = output, description="", color=myColor)
    await client.say(embed=embed)

@client.command(pass_context=True, name="dice")
async def dice(ctx):
    diceList = ["1", "2", "3", "4", "5", "6"]
    diceSelect = random.choice(diceList)
    answer = ((diceSelect) + " :game_die:")
    embed=discord.Embed(title=answer, description="", color=myColor)
    await client.say(embed=embed)

@client.command()
async def choose(*choice : str):
    embed=discord.Embed(title=(random.choice(choice)), description="", color=myColor)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def invite(ctx):
    embed=discord.Embed(title="", description="", color=myColor)
    embed.add_field(name="Invite me:", value="[Click here](https://discordapp.com/oauth2/authorize?client_id=466424854954901524&scope=bot&permissions=0)", inline=False)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def donate(ctx):
    embed=discord.Embed(title="", description="", color=myColor)
    embed.add_field(name="Donate:", value="[Click here](https://www.patreon.com/data_bot?alert=2)", inline=False)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def support(ctx):
    embed=discord.Embed(title="", description="", color=myColor)
    embed.add_field(name="Join support:", value="[Click here](https://discord.gg/ubEsUJH)", inline=False)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def upvote(ctx):
    embed=discord.Embed(title="", description="", color=myColor)
    embed.add_field(name="Upvote:", value="[Click here](https://discordbots.org/bot/466424854954901524/vote)", inline=False)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def botinfo(ctx):
    embed=discord.Embed(title="", description="", color=myColor)
    embed.add_field(name="Owner:", value="<@284487966347231232>", inline=True)
    embed.add_field(name="Version:", value=myVersion, inline=True)
    embed.add_field(name="Client ID:", value="466424854954901524", inline=True)
    embed.add_field(name="Guilds on this bot:", value="{} guilds".format(len(client.servers)), inline=True)
    embed.add_field(name="Users:", value=str(len(set(client.get_all_members()))), inline=True)
    embed.add_field(name="Donate:", value="[Click here](https://www.patreon.com/data_bot?alert=2)", inline=True)
    embed.add_field(name="Support:", value="[Click here](https://discord.gg/ubEsUJH)", inline=True)
    embed.add_field(name="Invite me:", value="[Click here](https://discordapp.com/oauth2/authorize?client_id=466424854954901524&scope=bot&permissions=0)", inline=True)
    embed.add_field(name="Upvote:", value="[Click here](https://discordbots.org/bot/466424854954901524/vote)", inline=True)
    embed.add_field(name="View client on DBL", value="[Click here](https://discordbots.org/bot/466424854954901524)", inline=True)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    embed=discord.Embed(title="Pong! {} MS :ping_pong:".format(round((t2-t1)*1000)), description="", color=myColor)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def hello(ctx):
    embed=discord.Embed(title="Hello there! :wave:", description="", color=myColor)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def kick(ctx, userName: discord.User):
    author = ctx.message.author
    if author.server_permissions.kick_members == True:
        await client.kick(userName)
        embed = discord.Embed(title=str(userName.name) + " was successfully kicked.", color=myColor)
        await client.say(embed=embed)
    if author.server_permissions.kick_members == False:
        permission_error = "Imposter! Your no admin!"
        embed = discord.Embed(title=permission_error, color=myColor)
        await client.say(embed=embed)
    author = ctx.message.author

@client.command(pass_context=True)
async def ban(ctx, userName: discord.User):
    author = ctx.message.author
    if author.server_permissions.ban_members == True:
        await client.ban(userName)
        embed = discord.Embed(title="Thy ban hammer has fallen upon" + str(userName.name) + ("!"), color=myColor)
        await client.say(embed=embed)
    if author.server_permissions.ban_members == False:
        permission_error = "Imposter! your no admin!"
        embed = discord.Embed(title=permission_error, color=myColor)
        await client.say(embed=embed)
    author = ctx.message.author

@client.command(pass_context=True)
async def clear(ctx, number):
    author = ctx.message.author
    if author.server_permissions.manage_messages == True:
        embed=discord.Embed(title="Deleted " + number + " messages!", color=myColor)
        mgs = []
        number = int(number)
        number + 1
        async for x in client.logs_from(ctx.message.channel, limit = number):
            mgs.append(x)
        await client.delete_messages(mgs)
        await client.say(embed=embed)
    if author.server_permissions.manage_messages == False:
        permission_error = "Imposter! Your no admin!"
        embed = discord.Embed(title=permission_error, color=myColor)
        await client.say(embed=embed)
    author = ctx.message.author

@client.command(pass_context=True)
async def learnPython(ctx):
    embed=discord.Embed(title="Tutorial from the basics of Python : https://automatetheboringstuff.com/.", description="", color=myColor)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def learnJava(ctx):
    embed=discord.Embed(title="Tutorial from the basics of Java : http://www.learnjavaonline.org/.", description="", color=myColor)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def learnJavaScript(ctx):
    embed=discord.Embed(title="Tutorial from the basics JavaScript : https://www.javascript.com/try.", description="", color=myColor)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def learnNodejs(ctx):
    embed=discord.Embed(title="Tutorial from the basics of Node.js: https://learnnode.com/.", description="", color=myColor)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def learnHTML(ctx):
    embed=discord.Embed(title="Tutorial from the basics of HTML : https://www.codecademy.com/learn/learn-html.", description="", color=myColor)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def learnDiscordpy(ctx):
    embed=discord.Embed(title="Discord.py is a library for Python that allows you to code Discord apps! To learn Discord.py, you must know some Python. Docs : http://discordpy.readthedocs.io/en/latest/api.html. Install Discord.py : `pip install discord.py` in a cmd.", description="", color=myColor)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def learnDiscordjs(ctx):
    embed=discord.Embed(title="Discord.js is a library for Node.js that allows you to code Discord apps! To learn Discord.js, you must know some Node.js. Official site : https://discord.js.org/#/. To install Discord.js, type `npm install discord.js` into a cmd!", description="", color=myColor)
    await client.say(embed=embed)

@client.command()
async def add(left : int, right : int):
    embed=discord.Embed(title="", description=(left + right), color=myColor)
    embed.set_footer(text=f'{left} + {right}')
    await client.say(embed=embed)

@client.command()
async def subtract(left : int, right : int):
    embed=discord.Embed(title="", description=(left - right), color=myColor)
    embed.set_footer(text=f'{left} - {right}')
    await client.say(embed=embed)

@client.command()
async def multiply(left : int, right : int):
    embed=discord.Embed(title="", description=(left * right), color=myColor)
    embed.set_footer(text=f'{left} x {right}')
    await client.say(embed=embed)

"""@client.command()
async def divide(left : int, right : int):
    embed=discord.Embed(title="", description=(left * right), color=myColor)
    embed.set_footer(text=f'{left} x {right}')
    await client.say(embed=embed)"""

client.run(token)
