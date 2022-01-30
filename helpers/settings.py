# (c) @AbirHasan2005

import asyncio
from helpers.database.access_db import db
from pyrogram.errors import MessageNotModified, FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def OpenSettings(m: Message, user_id: int):
    try:
        await m.edit(
            text="**⚙️⁩ تنظیمات را به دلخواه تغییر دهید 👇**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(f"📤 آپلود بصورت : {'| ویدیو |' if (await db.get_upload_as_doc(id=user_id)) is False else '| فایل |'} ✅", callback_data="triggerUploadMode")],
                    [InlineKeyboardButton(f"🎞️ Generate Sample Video {'✅' if (await db.get_generate_sample_video(id=user_id)) is True else '❌'}", callback_data="triggerGenSample")],
                    [InlineKeyboardButton(f"📸 گرفتن اسکرین شات ها : {'| ✅ فعال |' if (await db.get_generate_ss(id=user_id)) is True else '| ❌ غیرفعال |'}", callback_data="triggerGenSS")],
                    [InlineKeyboardButton("⭕ نمایش عکس سرصفحه ویدیو ⭕", callback_data="showThumbnail")],
                    [InlineKeyboardButton("× بستن ×", callback_data="close")]
                ]
            )
        )
    except MessageNotModified:
        pass
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await m.edit("**😑 You Are Spamming Dude!**")
    except Exception as err:
        raise err
