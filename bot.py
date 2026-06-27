import telebot
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda msg: True)
def reply(message):
    text = message.text
    if "سلام" in text or "درود" in text:
        bot.reply_to(message, "سلام! ربات لاغری و زیبایی!\nبنویسید:\n- رژیم\n- ورزش\n- آب\n- سایز\n- دمنوش\n- اندام\n- پوست\n- استایل\n- مو")
    elif "رژیم" in text:
        bot.reply_to(message, "رژیم لاغری:\n✅ صبحانه: تخم مرغ و سبزی\n✅ ناهار: مرغ و سالاد\n✅ شام: سبک و زود\n❌ نوشابه و شیرینی ممنوع!")
    elif "ورزش" in text:
        bot.reply_to(message, "ورزش روزانه:\n✅ پیاده روی 30 دقیقه\n✅ اسکات 3 ست\n✅ پلانک 30 ثانیه!")
    elif "آب" in text:
        bot.reply_to(message, "آب و لاغری:\n✅ 8 لیوان روزانه\n✅ صبح ناشتا با لیمو!")
    elif "سایز" in text or "شکم" in text:
        bot.reply_to(message, "کاهش سایز:\n✅ کمتر
