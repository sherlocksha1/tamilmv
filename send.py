import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

api = '5613970727:AAFvGY33k5mSXZ1IXnDCUG_pJjXTfo0oixM'
updater = Updater('5613970727:AAFvGY33k5mSXZ1IXnDCUG_pJjXTfo0oixM',use_context=True)
dispatcher = updater.dispatcher



def send(chatId,textMessage):
    bot = telegram.Bot(token=api)
    bot.sendMessage(chat_id=chatId,text=textMessage)
