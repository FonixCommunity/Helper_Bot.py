# FCC importation

from FCC.config import*

"""
* FCC.Config : stylesheet of cosole message

* FCC.info : information for the bot
"""

from FCC.info import BotInfo


# Module Importations


import discord
import asyncio
import os

from pystyle import*
from numpy import*


from discord import app_commands
from discord.ext import commands

# Contents of all commands

from Class_System.Class_Type import Bot_Self
from Class_System.SRV_EMOJI import Emojis_Server

"""

* Bot_Self : {Status & Avatar Change}

## Temporary ##

* SRV_EMOJI : {All Emojis}

## Out Of Temporary ##


"""

# Emebed Elements For All Commands

from Class_Embeds.Embed_Say import say_cmd

"""
* Embed Say : Embed Message For {Say Command}

"""

# Clear Console

os.system('cls')

# Welcome Messages

print(f"\n{W_U}\n")

# Guild as value

""" global GUI_ """

"""GUI = discord.Object(id=TYPESERVERID)"""

# Values for all commands

bot_base = commands.Bot(intents=discord.Intents.all(),command_prefix=BotInfo(TAG="PFX").CMDH)


# Statrtup

@bot_base.event
async def on_ready():
    global Statu
    global Emoji_Type

    Statu = Bot_Self(bot_base)
    Emoji_Type = Emojis_Server(visibility=True)

    print(f'\n{B_r}Bot is ready! Logged in as {bot_base.user} {CR}')

    bot_base.loop.create_task(Task_Runer_A())
    bot_base.loop.create_task(Task_Runer_B())

    bot_base.commands.update()

    try:
        asyn = await bot_base.tree.sync()
        print(f"\n{B_r} Synced {len(asyn)} Commands {CR}")
    except Exception as fe :
        print(fe)


async def Task_Runer_A():
    indexbrekerloop = 0
    
    while True:
        if indexbrekerloop < 100 :
            await asyncio.sleep(2)
            await Statu.Statu_Update(config=True)
            indexbrekerloop += 1
        elif indexbrekerloop > 100 :
            await Statu.Statu_Update(config=None)
            timeout = random.randint(43200, 86400)
            hour, reset = divmod(timeout, 3600)
            minutes, seconds = divmod(reset, 60)
            stoprun = discord.Activity(type=discord.ActivityType.watching, name=f"🤖 RateLimite Break For ({hour:02}h,{minutes:02}m,{seconds:02}s)")
            await bot_base.change_presence(status=discord.Status.dnd, activity=stoprun)
            await asyncio.sleep(timeout)
            indexbrekerloop = indexbrekerloop*0
        else : 
            continue



async def Task_Runer_B():
    while True:
        await asyncio.sleep(2)
        await Statu.Statu_Imge_Default(config=True)


# Creating Commands

@bot_base.command(name="stop", aliases=["Stop", "STOP"])
async def stop(ctx):
    if ctx.author.id == BotInfo(TAG="ID").IDTYPEDEV :
        await ctx.send(f"## {Emoji_Type.Dev_Icon}  Results {Emoji_Type.Alarm} :\n### {Emoji_Type.Engrenage} *_Bot Stoped_* {Emoji_Type.Engrenage}")
        await asyncio.sleep(1)
        await bot_base.close()
    else : 
        return
    

"""
* stop : {turn down that bot if aplication commands are available }

## Urgent command ##

* guildmanage : {clear obsolete guilds commands}

## Urgent command & renw slashe commands ##

"""
    
@bot_base.command(name='guildmanage', aliases=['cmd-nul', 'guildclear'])
async def delete_commands(ctx: discord.ext):
    if ctx.author.id == BotInfo(TAG="ID").IDTYPEDEV :
        bot_base.tree.clear_commands(guild=None)
        await bot_base.tree.sync()
        await ctx.send(f'### {Emoji_Type.Red_Arrow} **_All obsolete slash commands have been removed from the server_** {Emoji_Type.Bot_Badge}')
    else:
        return


"""/** @bot_base.tree.command(guild=GUI, name="down", description="To Stop The Bot 'AdminOnly'") **/"""


@bot_base.tree.command( name="down", description="To Stop The Bot 'Devloper'")
@app_commands.choices(choice=[app_commands.Choice(name="Yes", value="yes"), app_commands.Choice(name="No", value="no")])
@app_commands.describe(choice="True or False")
async def down(interaction: discord.Interaction, choice: app_commands.Choice[str]):
        if interaction.user.id ==  BotInfo(TAG="ID").IDTYPEDEV :
            if choice.value == "yes":
                RESP = f"## **{Emoji_Type.Red_Arrow} Results :**\n### {Emoji_Type.Dev_Badge} **_Bot Stoped_** {Emoji_Type.Waiting}."
                set = 0
            elif choice.value == "no":
                RESP= f"## {Emoji_Type.Red_Arrow} Results :\n### {Emoji_Type.Engrenage} **_Command Cancelled_** {Emoji_Type.Waiting}."
                set = 1
            else:
                RESP= f"## {Emoji_Type.Red_Arrow} **Error:** \n* **Type** : _**Argument**_\n* **Your Choice** **is {choice}** **_You Can Only Write `[True or False']`_**"
    
            await asyncio.sleep(2)
            await interaction.response.send_message(RESP)

            if set == 1:
                pass

            elif set == 0 :
                await asyncio.sleep(0.5)
                await bot_base.close()
        else:
             await interaction.response.send_message(content=f"### **_{Emoji_Type.Dev_Icon} Error {Emoji_Type.Alarm} :_**\n\n* **Role missing `DEV-BUSID`**")
        

"""/** @bot_base.tree.command("guild=GUI" name="update", description="Restart the bot 'Admin Only'") **/"""


@bot_base.tree.command( name="update", description="Restart the bot 'Devloper'")
@app_commands.choices(choice=[app_commands.Choice(name="Yes", value="yes"), app_commands.Choice(name="No", value="no")])
@app_commands.describe(choice="Yes or No")
async def update(interaction: discord.Interaction, choice: app_commands.Choice[str]):
    if interaction.user.id == BotInfo(TAG="ID").IDTYPEDEV:
        if choice.value == "yes":
            await interaction.response.send_message(content=f"{Emoji_Type.Red_Arrow} **Please wait...**")
            await asyncio.sleep(1)
            for i in range(100) :
                bot_base.commands.update()
                await interaction.edit_original_response(content=f"**{Emoji_Type.Waiting} {i+1}% {Emoji_Type.Engrenage}**")
            await interaction.edit_original_response(content=f"**{Emoji_Type.Waiting} Resume.... {Emoji_Type.Engrenage}**")
            await interaction.edit_original_response(content=f"### {Emoji_Type.Engrenage} ***Update Success*** {Emoji_Type.Cat_Spin}")
        else :
            await interaction.response.send_message(content=f"## {Emoji_Type.Red_Arrow} Resulte :\n### {Emoji_Type.Engrenage} **_Command Cancelled_** {Emoji_Type.Waiting}.")
    else :
            await interaction.response.send_message(content=f"### **_{Emoji_Type.Dev_Icon} Error {Emoji_Type.Alarm} :_**\n\n* **Role missing `DEV-BUSID`**")


"""/** @bot_base.tree.command(guild=GUI, name="say", description="say messages by the bot") **/"""


@bot_base.tree.command(name="say", description="say messages by the bot")
@app_commands.choices(color=[app_commands.Choice(name="Blue", value=discord.Color.blue().value), 
                              app_commands.Choice(name="Red", value=discord.Color.red().value),
                              app_commands.Choice(name="Green", value=discord.Color.green().value),
                              app_commands.Choice(name="Yellow", value=discord.Color.yellow().value),
                              app_commands.Choice(name="Blue", value=discord.Color.blue().value),
                              app_commands.Choice(name="Purpel", value=discord.Color.purple().value),
                              app_commands.Choice(name="Special", value=discord.Color.random().value)
                              ])

@app_commands.describe(title="Your Title",
                       message="Your Message", 
                       image_url="Choose An Image And Write Here Link",
                       color="We Have Some Colors Chose One",
                       preferance="The Image")

@app_commands.choices(preferance=[
    app_commands.Choice(name="With Image",value="yes"),
    app_commands.Choice(name="with Any Image",value="no")
                                 ])

async def say(interaction: discord.Interaction, 
              title: str = "Say command",
              message: str = "any message", 
              image_url: str = "https://cdn.dribbble.com/users/32512/screenshots/5276094/smile_loader_by_gleb.gif",  
              color: app_commands.Choice[int] = discord.Color.random().value,
              *,preferance: app_commands.Choice[str]):
    
    if preferance.value == "yes":

        author_name = interaction.user.name
        author_avatar = interaction.user.avatar

        if image_url.startswith('https://'):
            embed_say_WIM = await say_cmd.create_embed_with_image(
                User_Say=f"* **{message}**",
                User_IMG_URL=image_url,
                AUT_CH_TL=title,
                EMBD_CH_CL=color,
                Serv_IMG_URL=interaction.guild.icon.url,
                Aut=author_name,
                Aut_IM=author_avatar,
                Aut_LNK=interaction.channel.guild.id)
            await interaction.response.send_message(embeds=[embed_say_WIM])
        else:
            return
    elif preferance.value == "no" :
        author_name = interaction.user.name
        author_avatar = interaction.user.avatar

        embed_say_WNI = await say_cmd.create_embed_with_not_image(
            User_Say=f"* **{message}**",
            AUT_CH_TL=title,
            EMBD_CH_CL=color,
            Serv_IMG_URL=interaction.guild.icon.url,
            Aut=author_name,
            Aut_IM=author_avatar,
            Aut_LNK=interaction.channel.guild.id)
        await interaction.response.send_message(embeds=[embed_say_WNI])
    else :
        return

        
"""

/** // $ in dev $ // ** /

/** % Next Command % **/

/** >> Calculator << **/


"""

bot_base.run(BotInfo(TAG="TKN").TKNTYPE)