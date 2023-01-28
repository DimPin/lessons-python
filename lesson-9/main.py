from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint

token = '5708454167:AAGp2GFfRpeuSEZF9RTo9O5tEAyanFT3Hq8'

A = 0
B = 1

bot = Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher

def start(update, context):
    text = update.message.text

    if 'абв' in text.lower():
        context.bot.send_message(update.effective_chat.id, text.replace('абв', ''))
    else:
        context.bot.send_message(update.effective_chat.id, text)

start_handler = MessageHandler(Filters.text, start)

dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()