# 5432868362:AAFvpGlfGjGzGwg_YIqwPk982C9t9ZvfLzw
# Телеграмм бот рассказывающий анектоды с сайта 'https://www.anekdot.ru/'
import telebot
import requests, random
from bs4 import BeautifulSoup as b

URL = 'https://www.anekdot.ru/'
token = '5432868362:AAFvpGlfGjGzGwg_YIqwPk982C9t9ZvfLzw'


def anek(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]


joke = anek(URL)
random.shuffle(joke)

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['Start'])
def hai(message):
    bot.send_message(message.chat.id, 'Здраствуйте! Чтобы услышать анектод нажми цифру: ')


@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, joke[0])
        del joke[0]
    else:
        bot.send_message(message.chat.id, 'Введите цифру:: ')


bot.polling()
