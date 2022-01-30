# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    MONGODB_URI = os.environ.get("MONGODB_URI")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1445283714))

    START_TEXT = """
**👋 سلام {} عزیز خوش آمدید ❤

💢 با این ربات میتوانید چندین ویدیو را به یک ویدیو تبدیل کنید.

⛔️ فرمت های ویدیو باید یکسان باشد.

📚 راهنمای ربات : /help
⚙️ تنظیمات ربات : /settings

🤖 مدیر ربات : [FARSHIDBAND](https://t.me/FarshidBand)**
"""
    ABOUT_TEXT = """
★──────────∆──────────★
**🤖 نام ربات : [چسپاندن فایل های ویدیویی](https://t.me/ir_videomergeBot)

📢 کانال پشتیبانی : [+SERIES](https://t.me/SeriesPlus1)

👥 گروه پشتیبانی : [گروه](https://t.me/dlchinhub)

👨‍💻 سازنده ربات : [FﾑRSHIの-BﾑŊの](https://t.me/FarshidBand)

©️ @IR_VideoMergeBot ❤️**
★──────────∆──────────★
"""

    HELP_TEXT = """📚 راهنمای استفاده از ربات
 
**✵ ابتدا تنظیمات مربوطه را به دلخواه تغییر دهید 👈🏼 /settings **

**✵ فایل های خود را به این ربات ارسال کنید. 👀 حداکثر 2 تا 10 فایل **

**⚠️ فایل های ویدیویی که ارسال می کنید باید همه با یک فرمت باشد.**
مثال : اگر اولین فایلی که ارسال کردید با فرمت mp4 باشد باید بقیه فایل که میکنید با فرمت mp4 باشد.



🔮 @IR_VideoMergeBot ❤️**
"""
    
    CAPTION = "**__✅ @IR_VideoMergeBot ❤️__**"
    PROGRESS = """
**● ° {1} | of | {2} °**
**● درصد پروژه : {0}%**
**● سرعت : {3}/s**
**● تایم باقی مانده : {4}**
"""
