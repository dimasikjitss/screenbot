import config
import telebot
import screen
import validators


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, я Screen Bot. Отправь мне ссылку сайта и я сделаю его скриншот. Ввести нужно в формате: https://www.google.ru/ .")

@bot.message_handler(content_types=['text'])
def send_screenchot(message):
    if not validators.url(message.text):
        bot.send_message(message.chat.id, "Не правильно введенный формат, введите повторно в формате https://www.google.ru/")
    else:
        s = open(screen.screen_f(message.text),"rb") 
        bot.send_document(message.chat.id,s)

bot.polling(none_stop=True, interval=0)
