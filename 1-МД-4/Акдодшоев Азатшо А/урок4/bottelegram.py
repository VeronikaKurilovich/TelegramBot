import telebot

bot = telebot.TeleBot('5267263508:AAERjt4qR-xwnbUTlZQOqfA51RQHYkgUhbQ')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Э саламалейкум, я эхо-бот, напиши че-нбудь)')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'НЕ пиши мне больше: ' + message.text)

bot.polling(none_stop=True, interval=0)