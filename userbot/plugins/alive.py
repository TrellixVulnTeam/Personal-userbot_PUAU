"""Check if userbot alive or not . """
import os
import asyncio , time
from telethon import events
from userbot import StartTime
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP, catdef, catversion
from userbot.utils import admin_cmd,SUDO_CMD
from telethon import version
from platform import python_version, uname
import requests
import re
from PIL import Image
import nekos

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@Smart_S54"

ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
CAT_IMG = ALIVE_PIC

@borg.on(admin_cmd(outgoing=True, pattern="alive$"))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    uptime = await catdef.get_readable_time((time.time() - StartTime))
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()

    if CAT_IMG:
         cat_caption  = f"**🅿🅴🆁🆂🅾🅽🅰🅻 🅰🆂🆂🅸🆂🆃🅰🅽🆃 🆁🆄🅽🅽🅸🅽🅶 🆂🆄🅿🅴🆁🅵🅸🅽🅴**\n\n"
         cat_caption += f"**∂αтαвαѕє ѕтαтυѕ: (っ◔◡◔)っ ♥ Databases functioning normally!\n**"   
         cat_caption += f"☞𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐯𝐞𝐫𝐬𝐢𝐨𝐧 : `{version.__version__}\n`"
         cat_caption += f"☞𝐏𝐞𝐫𝐬𝐨𝐧𝐚𝐥 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `{catversion}`\n"
         cat_caption += f"☞𝐏𝐲𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `{python_version()}\n\n`"
         cat_caption += f"**𝐈'𝐦 𝐡𝐞𝐫𝐞 𝐭𝐨 𝐡𝐞𝐥𝐩 𝐲𝐨𝐮, 𝐦𝐲 𝐦𝐚𝐬𝐭𝐞𝐫!\n**"
         cat_caption += f"☞My Master: {DEFAULTUSER}\n"
         cat_caption += f"☞uptime : `{uptime}\n"
         await borg.send_file(alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id)
         await alive.delete()
    else:
        await alive.edit(f"**🅿🅴🆁🆂🅾🅽🅰🅻 🅰🆂🆂🅸🆂🆃🅰🅽🆃 🆁🆄🅽🅽🅸🅽🅶 🆂🆄🅿🅴🆁🅵🅸🅽🅴**\n\n"
                         "**∂αтαвαѕє ѕтαтυѕ: (っ◔◡◔)っ ♥ Databases functioning normally!\n**" 
                         f"☞𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐯𝐞𝐫𝐬𝐢𝐨𝐧 : `{version.__version__}\n`"
			 f"☞𝐏𝐞𝐫𝐬𝐨𝐧𝐚𝐥 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `{catversion}`\n"
                         f"☞𝐏𝐲𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `{python_version()}\n\n`"
                         "**𝐈'𝐦 𝐡𝐞𝐫𝐞 𝐭𝐨 𝐡𝐞𝐥𝐩 𝐲𝐨𝐮, 𝐦𝐲 𝐦𝐚𝐬𝐭𝐞𝐫!\n**"
                         f"☞My Master: {DEFAULTUSER}\n"
                         f"☞uptime : `{uptime}\n`"
                        )         
@borg.on(sudo_cmd(pattern="sudo", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    uptime = await catdef.get_readable_time((time.time() - StartTime))
    await event.reply(" SUDO COMMANDS ARE WORKING PERFECTLY \n\n"
                     f"☞𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐯𝐞𝐫𝐬𝐢𝐨𝐧 : `{version.__version__}\n"
                     f"☞𝐏𝐲𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `{python_version()}\n"
                     f"☞My Master: {DEFAULTUSER}\n"
                     f"**uptime :** `{uptime}\n`"
                     #"Deploy this userbot Now"
                    )

@borg.on(admin_cmd(pattern="cat$"))
async def _(event):
    await event.delete() 
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.cat()).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    img.seek(0)
    await bot.send_file(event.chat_id , open("temp.webp", "rb"),reply_to=reply_to_id) 
    
CMD_HELP.update({"alive": "`.alive` :\
      \nUSAGE: Type .alive to see wether your bot is working or not.\
      \n\n`.cat`\
      \n**USAGE : **Random cat stickers"
})
