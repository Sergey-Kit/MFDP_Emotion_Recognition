import time
import telebot
import subprocess
import io
import os
from PIL import Image

bot = telebot.TeleBot('6027285377:AAGdxHHwQAz-aBCmETy8GnDtfwumxWEckUM')


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет, отец!')


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # здесь можно получить информацию о фотографии
    photo = message.photo[-1] # получаем последнюю (самую большую) версию фотографии
    file_id = photo.file_id # получаем ID файла
    file_info = bot.get_file(file_id) # получаем информацию о файле
    downloaded_file = bot.download_file(file_info.file_path) # скачиваем файл

    # отправляем ответное сообщение
    bot.send_message(message.chat.id, 'Начал обработку..')

    # здесь можно обработать скачанный файл

    # создаем объект BytesIO из байтовой строки
    bytes_io = io.BytesIO(downloaded_file)

    # открываем изображение с помощью PIL
    image = Image.open(bytes_io)

    # сохраняем изображение в формате JPG
    image.save('./TG_imgs/image.jpg', 'JPEG')
    
    # отправляем ответное сообщение
    #bot.send_message(message.chat.id, 'Сохранил фото')

    result = subprocess.run(['python', 'emotion.py', './TG_imgs/image.jpg'],
                             stdout=subprocess.PIPE)
    #result = subprocess.run(['python', 'emotion.py', f'--photo={image}'],
    #                         stdout=subprocess.PIPE)
    # запускаем emotion.py и передаем ему путь к сохраненному файлу
    #result = os.popen('python emotion.py ' + file_name).read()  
    
    # отправляем ответное сообщение с результатом
    bot.send_message(message.chat.id, result.stdout.decode('utf-8'))

    # отправляем ответное сообщение
    bot.send_message(message.chat.id, 'Фотография получена и обработана')


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except ():
            time.sleep(5)