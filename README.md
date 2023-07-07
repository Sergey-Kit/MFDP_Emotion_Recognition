Обновление 31.05.23 : Добавлено выделение баундинг-бокса лица и его поворот, масштабирование и приведение координа с помощью RetinaFace

Обновление 03.06.23 : Запущен Telegram бот @Emotion_Recog_Bot. Отправляете ему фото с лицом человека, получаете эмоцию на лице и наличие азарта.

Обновление 06.07.23 : Добавлена обертка в Docker Telegram бота @Emotion_Recog_Bot.

# MFDP "Определение эмоций клиента казино"

Для погружения в тему была использованная предобученая NN ResNet18. 
Эту обученную модель для определения 7 эмоций на лицах взял тут (https://github.com/WIKI2020/FacePose_pytorch). 
Датасет EmotioNet (http://cbcsl.ece.ohio-state.edu/EmotionNetChallenge/) с размеченными эмоциями. На нем провалидировал вышеупомянутую модель.

## Demo
```
    # Запуск бота
    #Введите в консоли Linux
    sudo service docker start
    docker build -t <название бота> .
    docker run --env BOT_TOKEN=<токен вашего бота> <название бота> .

    # Бот запущен! Отправьте ему фото в телеграм.
```   

<img src="https://github.com/Sergey-Kit/MFDP_Emotion_Recognition/blob/main/img/absolute.jpg" width=30% height=30%>

![image](https://github.com/Sergey-Kit/MFDP_Emotion_Recognition/blob/main/img/power.jpg)

## Результаты

На данном этапе получил Confusion Matrix со приемлимыми метриками после добавления RetinaFace. 
Файл metrics.ipynb с Confusion Matrix

Было:
         ![image](https://github.com/Sergey-Kit/MFDP_Emotion_Recognition/blob/main/img/results.jpg)

Стало с RetinaFace:
![image](https://github.com/Sergey-Kit/MFDP_Emotion_Recognition/blob/main/img/results_v2.jpg)

Следующим этапом обучение собственной нейросети.

