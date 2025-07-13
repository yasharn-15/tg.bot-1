from flask import Flask, render_template_string
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")  # آدرس بعداً از render گرفته میشه

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <html>
    <body style="background-color: #f5f5dc; text-align: center;">
        <h1 style="color: #333;">Welcome to ETH-Miner</h1>
        <p style="color: #666;">Coming Soon...</p>
    </body>
    </html>
    """)

# ------------------------- Telegram Bot Logic -------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton("🟢 Open WebApp", web_app={"url": WEBAPP_URL})
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 Welcome! Click below to open the WebApp.", reply_markup=reply_markup)

def main():
    app_bot = Application.builder().token(BOT_TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.run_polling()

if __name__ == "__main__":
    from threading import Thread
    Thread(target=main).start()
    app.run(host="0.0.0.0", port=10000)
