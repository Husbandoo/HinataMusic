from pyrogram import Client, filters
from oda import app
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from oda.config import BOT_USERNAME, ASSUSERNAME, BOT_NAME
from oda.utils.filters import command


@app.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>✨ Welcome {message.from_user.first_name} - San!
        I am [{BOT_NAME}](https://t.me/{BOT_USERNAME}) Group Music Bot , Which Can Play Songs In Your Group Voice Chat In Easy Way
        
ɪ ʜᴀᴠᴇ ᴍᴀɴʏ ᴘʀᴀᴄᴛɪᴄᴀʟ ꜰᴇᴀᴛᴜʀᴇꜱ ʟɪᴋᴇ:\n
➥ ᴘʟᴀʏ ᴍᴜꜱɪᴄ.
➥ ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴏɴɢꜱ.
➥ ꜱᴇᴀʀᴄʜ ꜰᴏʀ ᴛʜᴇ ꜱᴏɴɢ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴘʟᴀʏ ᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ.\n
❓ ꜰɪɴᴅ ᴏᴜᴛ ᴀʟʟ ᴛʜᴇ ʙᴏᴛ'ꜱ ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ ➤ /help
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Add Hinata To Your Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                         "📣 Support", url=f"https://t.me/NexusXSupport"
                    ),
                    InlineKeyboardButton(
                        "🔎 Updates", url="https://t.me/TeamNexusX"
                    )
                ]
            ]
        ),
        
        PM_START_PIC = "https://te.legra.ph/file/92c305c99bde53b6378f1.jpg"
     disable_web_page_preview=False
    )


@app.on_message(command("help") & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.mention()}!
\n/play (song title/link/audio) — To Play the song you requested via YouTube
/song (song title) - To Download songs from YouTube
/yts (video title) — To Search Videos on YouTube with details
\n**Admins Only:**
/pause - To Pause Song playback
/resume - To resume playback of the paused song
/skip - To Skip playback of the song to the next Song
/end - To Stop Song playback
/cleandb - remove all queue
/userbotjoin - To Invite assistant to your chat
/broadcast - broadcast
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📣 Support", url="https://t.me/NexusXSupport"
                    ),
                    InlineKeyboardButton(
                        "🔎 Updates", url="https://t.me/TeamNexusX"
                    )
                ]
            ]
        )
    )
