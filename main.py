import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a link to shorten!")

async def shorten(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_link = update.message.text
    short_link = "https://example.com/ads?url=" + user_link
    await update.message.reply_text(f"Here is your short link:\n{short_link}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, shorten))

app.run_polling()
