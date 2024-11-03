from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# تعريف عنوان URL لصفحة الويب التي سيتم فتحها
WEB_URL = "https://your-web-page.com"

# دالة البداية لعرض زر "PLAY"
async def start(update: Update, context):
    user_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    # حفظ معرف المستخدم (ID) في المتغير
    user_data = {"user_id": user_id, "first_name": first_name}

    # إعداد زر "PLAY"
    keyboard = [
        [InlineKeyboardButton("PLAY", callback_data='play')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # إرسال رسالة تحتوي على زر "PLAY"
    await update.message.reply_text(
        text="Welcome! Click the button below to start playing:",
        reply_markup=reply_markup
    )

# دالة تعالج ضغط المستخدم على زر "PLAY"
async def button_click(update: Update, context):
    query = update.callback_query
    user_id = query.from_user.id

    # بناء URL مع معرف المستخدم (ID)
    redirect_url = f"{WEB_URL}/?user_id={user_id}"

    # توجيه المستخدم إلى URL
    await query.answer()
    await query.message.reply_text(
        f"Hello! You are being redirected...",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Go to URL", url=redirect_url)]
        ])
    )

# إعداد التطبيق والبوت
app = ApplicationBuilder().token('7696140362AAFt9GFPis9KwGGvZE93Fd8IXKhgxnzHQOE').build()

# ربط الأوامر والدوال مع البوت
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_click, pattern='play'))

# بدء تشغيل البوت
app.run_polling()
