import config
import telebot
import __init__
import procfile

token = config.token
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'find'])
def main(message):
    bot.send_message(message.chat.id, 'Ура, я жив')


if __name__ == '__main__':
     bot.polling(none_stop=True)
