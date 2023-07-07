import time
import telebot
import subprocess
import io
import os
from PIL import Image

bot_token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Отправьте фото клиента казино на обработку')


@bot.message_handler(content_types=['photo'])
def handle_photo(message):

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

    # To use without RetinaFace
    #image = cv2.imread(args.img)
    #image = image[:, :, ::-1]

    image_path = './TG_imgs/image.jpg'
    result = subprocess.run(['python', 'emotion.py', f'--photo={image_path}'], stdout=subprocess.PIPE)

    # Для работы с файлами из бота без докера
    #result = subprocess.run(['python', 'emotion.py', './TG_imgs/image.jpg'],
    #                         stdout=subprocess.PIPE)
    # Для работы с файлом на компьютере
    #result = subprocess.run(['python', 'emotion.py', f'--photo={image}'],
    #                         stdout=subprocess.PIPE)
    # Для работы с файлами на компьютере
    # запускаем emotion.py и передаем ему путь к сохраненному файлу
    #result = os.popen('python emotion.py ' + file_name).read()  
    
    # отправляем ответное сообщение с результатом
    
    excitement = {
        "Surprise\n": "Удивление",
        "Happiness\n": "Счастье",
        "Anger\n": "Злость",
        "Fear\n": "Страх",
        "Disgust\n": "Отвращение",
        "Neutral\n": "Нейральная",
        "Sadness\n": "Грусть",
        "": "Ошибка",
    }

    excitement_levels = {
        "Surprise\n": "Азарт высокий!",
        "Happiness\n": "Азарт высокий!",
        "Anger\n": "Азарт высокий!",
        "Fear\n": "Азарт низкий!",
        "Disgust\n": "Азарт низкий!",
        "Neutral\n": "Азарт низкий!",
        "Sadness\n": "Азарт низкий!",
        "": "Попробуйте другое фото"
    }

    output_excitement = result.stdout.decode('utf-8')
    bot.send_message(message.chat.id, f'Эмоция: {excitement[output_excitement]}')

    if output_excitement in excitement_levels:
        bot.send_message(message.chat.id, excitement_levels[output_excitement])

    # отправляем ответное сообщение
    bot.send_message(message.chat.id, 'Фотография получена и обработана')


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except ():
            time.sleep(5)