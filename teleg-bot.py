import config
import telebot
import screen
import validators

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Отправь мне ссылку сайта и я сделаю его скриншот:")

@bot.message_handler(content_types=['text'])
def send_screenchot(message):
    if not validators.url(message.text):
        bot.send_message(message.chat.id, "Не правильно введенный формат URL, введите повторно в формате https://www.google.ru/")
    else:
        # bot.send_chat_action(message.chat.id, 'typing')  
        # ex = screen.screen_f(message)  
        bot.send_photo(message.chat.id, photo=open('title.png', 'rb'))


bot.polling()



















# @bot.message_handler(commands=["start"])
# def hello_messages(message): 
#     bot.send_message(message, "Howdy, how are you doing?")

# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): 
# # Название функции не играет никакой роли, в принципе
#     bot.send_message(message.chat.id, message.text)

# if __name__ == '__main__':
#     bot.polling(none_stop=True)

# import pyscreenshot as ImageGrab

# if __name__ == "__main__":

#     # grab fullscreen
#     im = ImageGrab.grab()

#     # save image file
#     im.save("fullscreen.png")
# from pyvirtualdisplay import Display
# from selenium import webdriver   

# op = webdriver.ChromeOptions()
# op.add_argument('--headless')
# op.add_argument("--window-size=1440x1024")

# chromedriver = '/Users/maliboo/Downloads/chromedriver'
# driver = webdriver.Chrome(chromedriver,options=op)
# driver.get('https:/google.com/')
# driver.save_screenshot(driver.title+".png")

# driver.quit()

