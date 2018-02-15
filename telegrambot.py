__author__ = 'SSDorofeev'

import telegram
import logging
import telegram.ext
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

# g_vars
###################################
g_text_notauthorized = "Для продолжения работы с ботом вам необходимо авторизоваться. Для этого, пожалуйста, предоставьте свой контакт и паспортные данные"
g_text_authorized = "Кажется, вы авторизованы. Продолжаем!"
###################################

mybot = telegram.Bot(token='464876596:AAFaW8bdmy29hLdym8vMzN5fD9j5kT01GkQ')

updater = Updater(token='464876596:AAFaW8bdmy29hLdym8vMzN5fD9j5kT01GkQ')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


print(mybot.get_me())


def start(mybot, update):
     chat_id=update.message.chat_id
     print(chat_id)
     try:
         l_authorized_session = open(authorized_sessions.txt,'rw')
         for line in l_authorized_session do:
             if line.find(chat_id != -1)


    except IOError:
        print('File %s not exists' %)
    mybot.send_message(chat_id, text=g_text_notauthorized)
    print(chat_id)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def test(mybot, update):
    chat_id=update.message.chat_id
    mybot.send_message(chat_id, text='something text like')

text_handler = MessageHandler(Filters.text, test)
dispatcher.add_handler(text_handler)

def echo(mybot, update):
    mybot.send_message(chat_id=update.message.chat_id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


def keyboard(mybot, update):
    location_keyboard = telegram.KeyboardButton(text="send_location", request_location=True)
    contact_keyboard = telegram.KeyboardButton(text="send_contact", request_contact=True)
    custom_keyboard = [[ location_keyboard, contact_keyboard ]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    mybot.send_message(chat_id=update.message.chat_id, text="Would you mind sharing your location and contact with me?", reply_markup=reply_markup)

keyboard_handler = CommandHandler('keyboard', keyboard)
dispatcher.add_handler(keyboard_handler)
updater.start_polling()


def unknown(mybot, update):
    mybot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)