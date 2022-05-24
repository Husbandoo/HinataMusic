from pyrogram import Client, filters
from oda import app
from pyrogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from oda.utils.filters import command
from oda.Naruto import PM_START_PIC, PM_START_TEXT

PM_START_PIC = "https://telegra.ph/file/92c305c99bde53b6378f1.jpg"


@app.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        PM_START_PIC,
        caption=PM_START_TEXT,
        parse_mode="markdown",
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
                        "🔎 Updates", url="https://t.me/TeamNexusX")
                  ],[
                    InlineKeyboardButton(
                        "Bot Owner", url="https://t.me/Husbandoo"
                    ),
                    InlineKeyboardButton(
                        "Aogiri", url="https://t.me/AogiriNetwork"
                    )
                ]
            ]
        ),
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
