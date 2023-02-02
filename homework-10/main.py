from telegram  import Bot, Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

TOKEN = '5708454167:AAGp2GFfRpeuSEZF9RTo9O5tEAyanFT3Hq8'

updater = Updater(TOKEN)
bot = Bot(TOKEN)
dispatcher = updater.dispatcher

def start(update:Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, 'Привет')

def SearchingNumbers(data, operate):
    numberFirst = data[operate - 1]
    numberSecond = data[operate + 1]

    first = operate - 1
    second = operate + 2

    if data[operate] == '/':
        res = numberFirst / numberSecond
    elif data[operate] == '*':
        res = numberFirst * numberSecond
    elif data[operate] == '-':
        res = numberFirst - numberSecond
    elif data[operate] == '+':
        res = numberFirst + numberSecond
    
    result = data[0:first]
    result.append(res)
    result += data[second:len(data)]
    return result

def start_calc(update: Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, 'Введите выражение через пробел')

def add_data(user_id, text1, text):
    with open('homework-10/data_base.txt', 'a') as path:
        path.write(f'{user_id}; {text1}; {text}\n')

def calc(update: Update, context: CallbackContext):
    text1 = update.message.text
    text = update.message.text.split()
    
    for i in range(len(text)):
        if text[i].isdigit():
            text[i] = int(text[i])

    operations = ['/', '*', '-', '+']
    for i in range(len(operations)):
        j = 0
        while j in range(len(text)):
            if text[j] == operations[i]:
                operate = j
                text = SearchingNumbers(text, operate)
                j -= 2
            j += 1

    context.bot.send_message(update.effective_chat.id, *text)

    user_id = update.message.from_user.id
    add_data(user_id, text1, *text)

start_handler = CommandHandler('start', start)
start_calc_handler = CommandHandler('start_calc', start_calc)
calc_handler = MessageHandler(Filters.text, calc)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(start_calc_handler)
dispatcher.add_handler(calc_handler)

updater.start_polling()
updater.idle()