import config
import telebot
import json
import __init__
import procfile

token = config.token
bot = telebot.TeleBot(token)
tag = ''
phrase = ''

@bot.message_handler(commands=['start', 'find'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!Введи слово и я выдам тебе цитату.')
    
if __name__ == '__main__':
     bot.polling(none_stop=True)
