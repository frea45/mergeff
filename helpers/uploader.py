# (c) @AbirHasan2005
import asyncio
import time
from configs import Config
from helpers.database.access_db import db
from helpers.display_progress import progress_for_pyrogram, humanbytes
from humanfriendly import format_timespan
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


async def UploadVideo(bot: Client, cb: CallbackQuery, merged_vid_path: str, width, height, duration, video_thumbnail, file_size):
    try:
        sent_ = None
        if (await db.get_upload_as_doc(cb.from_user.id)) is False:
            c_time = time.time()
            sent_ = await bot.send_video(
                chat_id=cb.message.chat.id,
                video=merged_vid_path,
                width=width,
                height=height,
                duration=duration,
                thumb=video_thumbnail,
                caption=f"**● {merged_vid_path.rsplit('/', 1)[-1]}**" + f"\n\n{Config.CAPTION}",
                progress=progress_for_pyrogram,
                progress_args=(
                    "**📤 در حال آپلود ویدیو ...**",
                    cb.message,
                    c_time
                ),
                reply_markup=InlineKeyboardMarkup(
                    [[
                         InlineKeyboardButton("💬 ارسال نظرات و پیشنهادات", url="https://t.me/FarshidBand")]
                    ]
                )
            )
        else:
            c_time = time.time()
            sent_ = await bot.send_document(
                chat_id=cb.message.chat.id,
                document=merged_vid_path,
                caption=f"**● {merged_vid_path.rsplit('/', 1)[-1]}**" + f"\n\n{Config.CAPTION}",
                thumb=video_thumbnail,
                progress=progress_for_pyrogram,
                progress_args=(
                    "**📤 Uploading as Document...**",
                    cb.message,
                    c_time
                ),
                reply_markup=InlineKeyboardMarkup(
                    [[
                         InlineKeyboardButton("👀 More Amazing Botz 🤖", url="https://t.me/tellybots")]
                    ]
                )
            )
        await asyncio.sleep(Config.TIME_GAP)
        forward_ = await sent_.forward(chat_id=Config.LOG_CHANNEL)
        await forward_.reply_text(
            text=f"**• کاربر :** [{cb.from_user.first_name}](tg://user?id={str(cb.from_user.id)})\n**• نام کاربری :** `{cb.from_user.username}`\n**• آیدی عددی کاربر :** `{cb.from_user.id}`",
            disable_web_page_preview=True,
            quote=True
        )
    except Exception as err:
        print(f"**Failed to Upload Video!**\n**Error: {err}**")
        try:
            await cb.message.edit(f"**Failed to Upload Video!**\n**Error:**\n`{err}`")
        except:
            pass
