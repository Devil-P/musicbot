# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#https://t.me/
#https://t.me/
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from DaisyXMusic.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from DaisyXMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✘ α∂∂ мє тσ ʏօʊʀ ɢʀօʊρ ✘, url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "❖ Uρ∂αȶɛ Cɦαηηɛℓ ❖", url=f"https://t.me/Team_Memories"), 
                    InlineKeyboardButton(
                        "♬ ʂʊppօʀȶ ƈɦαȶ ♬", url=f"https://t.me/Team_Memories_Support")
                ],[
                    InlineKeyboardButton(
                        "☠ Ꭾσωєя∂ ɮʏ ☠", url=f"https://t.me/TeamRedxSkull")
                ] ,[
                    InlineKeyboardButton(
                        "😈♛︎ ᴍϒ Ơԝƞɛʀ ♛︎ 😈", url=f"https://t.me/Rohit_Xy")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**🔴 {PROJECT_NAME} is online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                      "♬ ʂʊppօʀȶ ƈɦαȶ ♬", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '▶️', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton("✘ α∂∂ мє тσ ʏօʊʀ ɢʀօʊρ ✘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = '❖ Uρ∂αȶɛ Cɦαηηɛℓ ❖', url=f"https://t.me/{UPDATES_CHANNEL}"),
             InlineKeyboardButton(text = '♬ ʂʊppօʀȶ ƈɦαȶ ♬', url=f"https://t.me/{SUPPORT_GROUP}")],
            [InlineKeyboardButton(text = ' ☠ Ꭾσωєя∂ ɮʏ ☠', url=f"https://{SOURCE_CODE}")],[
                    InlineKeyboardButton(
                        "😈♛︎ ᴍϒ Ơԝƞɛʀ ♛︎ 😈", url=f"https://t.me/Rohit_Xy")
                ],[InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '▶️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**🙋‍♀️ Hello there! I can play music in the voice chats of telegram groups & channels.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🟡 Click here for help 🟡", url=f"https://t.me/{BOT_USERNAME}?start"
                    )
                ]
            ]
        ),
    )




