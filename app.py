from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext

# ضع توكن البوت هنا
BOT_TOKEN = "7696140362AAFt9GFPis9KwGGvZE93Fd8IXKhgxnzHQOE"
WEB_APP_URL = "https://your-web-app-url.com"  # ضع رابط تطبيق الويب هنا

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton(
                text="Play", web_app={"url": WEB_APP_URL}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Click Play to start!", reply_markup=reply_markup)

async def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
