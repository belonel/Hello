import config
import telebot
import logging

token = config.token
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'find'])
def main(message):
    try:
        bot.send_message(message.chat.id, 'Привет!Введи слово и я выдам тебе цитату.')
    except:
        log.exception("Error!")
    
if __name__ == '__main__':
     bot.polling(none_stop=True)
