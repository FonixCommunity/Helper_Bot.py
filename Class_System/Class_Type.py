
import discord
from discord.ext import commands

from FCC.Numbers import nbtf,nbtb,nbtc,nbtd
from FCC.Status import ListEmoji,ListCommand,ListGame,ListText


from Class_System.FCT_IMG import*

from FCC.config import*
from FCC.info import BotInfo

import asyncio

bot_base = commands.Bot(intents=discord.Intents.all(),command_prefix=BotInfo(TAG="PFX").CMDH)


class Bot_Self :
    def __init__(self, bot_base):
            self.bot_base = bot_base

    async def Statu_Update(self , config: tuple):

        print(f"\n{B_r} File Class_Runer Executed For Statue{CR}\n")

        if config == None:
            print(f"\n{New} Return Type Error {CR}\n")
            print(f"\n{F_r}{config} argument{CR}\n\n{E_R}{CR}\n")
            return all
        
        elif config == True :
            print(f"\n{New} Return Type True For Statues Runer{CR}\n")
            while True:

                    for i in range(nbtb):
                        getgamename = random.choice(ListGame)

                    for i in range(nbtc):
                        getemoji = random.choice(ListEmoji)

                    for i in range(nbtf):
                        gettext = random.choice(ListText)
            
                    for i in range(nbtd):
                        getcmdtext = random.choice(ListCommand)

                    statuetegame = f"\n{getemoji}{getgamename}{getemoji}"
                    statuecmd = f"\n{getcmdtext}"

                    Lesting_Statu_Type = discord.Activity(type=discord.ActivityType.listening, name="🤖 Bot In Dev 💻" )
                    Watching_Statu_Type = discord.Activity(type=discord.ActivityType.watching, name=f"\n\n{statuecmd}")
                    Playing_Statu_Type = discord.Activity(type=discord.ActivityType.playing, name=f"\n\n{statuetegame}")
                    F_Activity_Statu_Type = discord.Activity(type=discord.ActivityType.competing,name=f"\n\n{gettext}")

                    await asyncio.sleep(1)
                    await self.bot_base.change_presence(activity=Playing_Statu_Type,status=discord.Status.idle)
                    await asyncio.sleep(2)
                    await self.bot_base.change_presence(activity=Lesting_Statu_Type, status=discord.Status.do_not_disturb)
                    await asyncio.sleep(3)
                    await self.bot_base.change_presence(activity=Watching_Statu_Type, status=discord.Status.online)
                    await asyncio.sleep(4)
                    await self.bot_base.change_presence(activity=F_Activity_Statu_Type,status=discord.Status.online)
                    await asyncio.sleep(5)
        else : 
             return ValueError("Error Type: %f")

    async def Statu_Imge_Default(self , config):
            print(f"\n{B_r} File Class_Runer Executed For Statue Type Statu_Image_Default -random{CR}\n")
            if config  == None: 
                print(f"\n{New} Return Type Error {CR}\n")
                print(f"\n{F_r}{config} is not available{CR}\n")
                return False 
            elif config != None :
                print(f"\n{New} Return Type True For Statues Runer{CR}\n")
                img = [img_type_A, img_type_B, img_type_C]
            else : return ValueError("Error Type: %f")
            
            while True :
                    await asyncio.sleep(46200)
                    pp = random.choice(img)
                    await self.bot_base.user.edit(avatar=pp)
                    await asyncio.sleep(10)