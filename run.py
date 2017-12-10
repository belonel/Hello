import config
import telebot

token = config.token
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'find'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!Введи слово и я выдам тебе цитату.')
    
if __name__ == '__main__':
     bot.polling(none_stop=True)
