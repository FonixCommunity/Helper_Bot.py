import datetime
import discord
from discord.app_commands import Choice
from Class_System.SRV_EMOJI import Emojis_Server as SE


# Variables

IMJ = SE(visibility=True)
now = datetime.datetime.now()

# Class Creation

"""
# Say Command #

* With Embed

=> Our Prameter For 'create_embed : @with_image/@with_not_image'

/** User_Say : (user message) **/
/** User_IMG_URL : (user image url choice) **/
/** AUT_CH_URL : (user title choice for here embed) **/
/** EMBD_CH_CL : (user color choice for here embed from the colors list) **/
/** Serv_IMG_URL : (server image url) **/
/** Aut : (user name) **/
/** Aut_IM : (user profile picture image url) **/
/** Aut_LNK : (the channel id §for a link§) **/

=> Ther Argument Is On <index.py> file


"""

class say_cmd:

    """
    # Create Embed With Image #

    * Parameter 'User_IMG_URL' existing (The image URL that user chose because  [properties choice ^Image^])
    """

    @staticmethod
    async def create_embed_with_image(User_Say: str = None, 
                     User_IMG_URL: str = None, 
                     AUT_CH_TL: str = None, 
                     EMBD_CH_CL: Choice = None,
                     Serv_IMG_URL: str = None, 
                     Aut: str=None, 
                     Aut_IM: str=None,
                     Aut_LNK: str = None 
                     ) -> discord.Embed:
        say_embed_wim = discord.Embed()
        if User_Say is not None and User_IMG_URL is not None and AUT_CH_TL is not None and EMBD_CH_CL is not None and Serv_IMG_URL is not None:
            say_embed_wim.set_author(name=Aut, url=f"https://discord.com/channels/{Aut_LNK}" ,icon_url=Aut_IM)
            say_embed_wim.title = f"{IMJ.Red_Arrow} {AUT_CH_TL}"
            say_embed_wim.color = EMBD_CH_CL.value if isinstance(EMBD_CH_CL, Choice) else EMBD_CH_CL
            say_embed_wim.description = f"{User_Say}"
            say_embed_wim.timestamp = now
            say_embed_wim.set_thumbnail(url=f"{Serv_IMG_URL}")
            say_embed_wim.set_image(url=f"{User_IMG_URL}")
            say_embed_wim.set_footer(icon_url="https://i.pinimg.com/originals/06/60/ef/0660efe82fa3da42ed56eef013171835.gif",
                                 text="Created By FonixCommunity")
            
        return say_embed_wim
            
    """
    # Create Embed With Any Image #

    * Parameter 'User_IMG_URL' not existing (The image is none because it [properties choice ^NoImage^])
    """
    @staticmethod
    async def create_embed_with_not_image(
                User_Say: str = None, 
                AUT_CH_TL: str = None, 
                EMBD_CH_CL: Choice = None,
                Serv_IMG_URL: str = None, 
                Aut: str=None, 
                Aut_IM: str=None,
                Aut_LNK: str = None 
            ) -> discord.Embed:
            say_embed_wnm = discord.Embed()
            if User_Say is not None and AUT_CH_TL is not None and EMBD_CH_CL is not None and Serv_IMG_URL is not None:
                say_embed_wnm.set_author(name=Aut, url=f"https://discord.com/channels/{Aut_LNK}" ,icon_url=Aut_IM)
                say_embed_wnm.title = f"{IMJ.Red_Arrow} {AUT_CH_TL}"
                say_embed_wnm.color = EMBD_CH_CL.value if isinstance(EMBD_CH_CL, Choice) else EMBD_CH_CL
                say_embed_wnm.description = f"{User_Say}"
                say_embed_wnm.timestamp = now
                say_embed_wnm.set_thumbnail(url=f"{Serv_IMG_URL}")
                say_embed_wnm.set_footer(icon_url="https://i.pinimg.com/originals/06/60/ef/0660efe82fa3da42ed56eef013171835.gif",
                                 text="Created By FonixCommunity")
                
            return say_embed_wnm