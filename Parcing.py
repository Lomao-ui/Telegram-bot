import random
import requests
from bs4 import BeautifulSoup as project
from time import sleep
import random
import telebot
from telebot import types
from dotenv import load_dotenv
import os
def func(url):
    sleep(3)
    response = requests.get(url).text
    soup = project(response, 'lxml')
    result = soup.find_all('div', class_='text')
    joke = []
    for elem in result:
        result_end = elem.text.strip()
        joke.append(result_end)
    return joke

load_dotenv()
Apy_key = os.getenv('Token')
URl = os.getenv('Url')

result = func(URl)
random.shuffle(result)

bot = telebot.TeleBot(Apy_key)


def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_start = types.KeyboardButton('/start')
    markup.add(item_start)
    bot.send_message(message.chat.id, 'Добро пожаловать! Нажмите кнопку /start', reply_markup=markup)


# Функция для отправки анекдотов по запросу пользователя

@bot.message_handler(content_types=['text'])
def jokes(message):
    with open('user_messages.txt', 'a', encoding='utf-8') as user_messages_file:
        user_messages_file.write(f'{message.chat.id}: {message.text}\n')
        if message.text.lower() in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # Проверяем, есть ли еще анекдоты в списке
            if result:
                bot.send_message(message.chat.id, result[0])
                del result[0]  # Удаляем отправленный анекдот из списка
            else:
                bot.send_message(message.chat.id, 'Больше анекдотов нет!')
        else:
            bot.send_message(message.chat.id, 'Введите любую цифру от 1 до 9: ')


# Запускаем бота
bot.polling()
