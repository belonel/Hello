import telebot
import __init__
import procfile

token = token='497421683:AAHtSmzXBBGqHoPuJ-zR7qOd97NwWUEWqIM'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'find'])
def main(message):
    bot.send_message(message.chat.id, 'Ура, я жив')


if __name__ == '__main__':
     bot.polling(none_stop=True)
