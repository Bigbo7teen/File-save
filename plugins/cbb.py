#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐅𝐞𝐞 : 5000/= per month\n\n○ 𝐌𝐨𝐛𝐢𝐥𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 🇺🇬 : <code>0704312951</code> (Andrew Kawuki)\n\n○ 𝐎𝐧𝐥𝐢𝐧𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 : <a href='https://flutterwave.com/pay/lflix_premium'>Flutterwave </a>\n\n○ 𝐍𝐎𝐓𝐄 : After successful payment, send the screenshot to 👇\n................... <a href='https://t.me/andyganiso'>【L-FLIX ADMIN】</a>\n\n○ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : @katandika2022\n\n○ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 : @katandika2023</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
