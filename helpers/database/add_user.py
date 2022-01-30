# (c) @AbirHasan2005

from configs import Config
from helpers.database.access_db import db
from pyrogram import Client
from pyrogram.types import Message


async def AddUserToDatabase(bot: Client, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
        if Config.LOG_CHANNEL is not None:
            await bot.send_message(
                int(Config.LOG_CHANNEL),
                f"#کاربر_جدید : \n\n👤 کاربر جدید [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id}) وارد ربات شد. @{(await bot.get_me()).username} !!"
            )
