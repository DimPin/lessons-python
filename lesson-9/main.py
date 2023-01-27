from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint

token = '5708454167:AAGp2GFfRpeuSEZF9RTo9O5tEAyanFT3Hq8'

A = 0
B = 1

bot = Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет \n Как дела?")
    return A

def howareu(update, context):
    text = update.message.text
    if 'хор' in text.lower():
        context.bot.send_message(update.effective_chat.id,"Я рад, что у вас всё хорошо")
    else:
        context.bot.send_message(update.effective_chat.id,"Не грусти, всё будет отлично")
    context.bot.send_message(update.effective_chat.id,"Какая у тебя погода?")
    return B

def weather(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id,"У меня сегодня такая же погода")
    context.bot.send_message(update.effective_chat.id,"Мне пора бежать, пока!")
    return ConversationHandler.END

def cancel (update, context):
    context.bot.send_message(update.effective_chat.id,"Что то пошло не так")

start_handler = CommandHandler('start', start)
howareu_handler = MessageHandler(Filters.text, howareu)
weather_handler = MessageHandler(Filters.text, weather)
cancel_handler = CommandHandler("cancel", cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                        states={A: [howareu_handler],
                                        B: [weather_handler]}, 
                                        fallbacks= [cancel_handler])


dispatcher.add_handler(conv_handler)


updater.start_polling()
updater.idle()