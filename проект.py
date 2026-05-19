import telebot
import os
API_TOKEN = '8665282355:AAEh9MiOuQ5m4jZGGMQg64k5WbVfet3i9Vc'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message, "Привет! Я бот для рассписания. ЧТО ХОЧЕШЬ?")

@bot.message_handler(commands=['set_schedule'])
def handle_photo(message):
    photo = message.photo[-1]
    day_of_week = message.text
    file_id = photo.file_id
    file_path = bot.get_file(file_id).file_path
    downloaded_file = bot.download_file(file_path)
    save_path = f'schedule_{day_of_week}'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_name = f'{day_of_week}.jpg'
    with open(os.path.join(save_path, file_name), 'wb') as new_file:
        new_file.write(downloaded_file)
   

@bot.message_handler(commands=['get_schedule'])
def text(message):
    bot.send_message(message, "Держи рассписание друн!")
    day_of_week = message.text
    save_path = f'schedule_{day_of_week}'
    file_name = f'{day_of_week}.jpg'

    bot.send_photo(message.chat.id, open(os.path.join(save_path, file_name), 'rb'))

