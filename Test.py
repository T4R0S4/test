from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import os

TOKEN = os.getenv("7773033342:AAGRCYkQufSs5zxrAxzvSJoyysGXwcR8v2o")  # Mengambil token dari environment variable

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Halo! Bot Telegram Railway berjalan!')

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
