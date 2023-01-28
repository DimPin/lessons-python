from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint

token = '5708454167:AAGp2GFfRpeuSEZF9RTo9O5tEAyanFT3Hq8'

bot = Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет\nКак дела?')

def random(update, context):
    context.bot.send_message(update.effective_chat.id, f'{randint(1, 100)}')

def defult(update, context):
    context.bot.send_message(update.effective_chat.id, 'Я не умею разговаривать')

def privet(update, context):
    text = update.message.text
    if 'прив' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'Привет, друг')
    else:
        context.bot.send_message(update.effective_chat.id, 'Я не понимаю')

start_handler = CommandHandler('start', start)
random_handler = CommandHandler('random', random)
defult_handler = MessageHandler(Filters.voice, defult)
privet_handler = MessageHandler(Filters.text, privet)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(random_handler)
dispatcher.add_handler(defult_handler)
dispatcher.add_handler(privet_handler)

updater.start_polling()
updater.idle()