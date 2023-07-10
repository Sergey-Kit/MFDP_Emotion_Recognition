# MFDP "Определение эмоций клиента казино"

Данная ветка для исследования включает в себя: 
Скрипт (emotion.py) по обработке одного изображения с хоста с указанием пути изображения. В результат выводится эмоция на лице. 
Скрипт валидации (emotion_loop.py) для обработки потока изображений из интернета посредством HTTP запросов на адреса указанные в Excel-файле (из датасета EmotioNET)

Обновление 31.05.23 : Добавлено выделение баундинг-бокса лица и его поворот, масштабирование и приведение координа с помощью RetinaFace

Обновление 03.06.23 : Запущен Telegram бот [@Emotion_Recog_Bot](https://t.me/emotion_recog_bot). Отправляете ему фото с лицом человека, получаете эмоцию на лице и наличие азарта. Код бота в соответствующей ветке.

Для погружения в тему была использованная предобученая NN ResNet18. 
Эту обученную модель для определения 7 эмоций на лицах взял тут (https://github.com/WIKI2020/FacePose_pytorch). 
Датасет EmotioNet (http://cbcsl.ece.ohio-state.edu/EmotionNetChallenge/) с размеченными эмоциями. На нем провалидировал вышеупомянутую модель.

## Demo
```
    # install requirements
    First install python 3.7,and then:
    pip install requirements.txt
    Download the emoticon model (the angle model is already in the code):
    [https://pan.baidu.com/s/1oxznkRcP5w8lzYMAjj87-w],accesscode:WIKI
    
    # run the simple inference script(emotion_loop)
    Download the emoticon model into checkpoint file
    CUDA_VISIBLE_DEVICE=0 python emotion_loop.py
```   
Потоком сохраняются изображения из интернета и валидируются моделью. Результат сохраняется в Excel-файл.

```
    # run the simple inference script(emotion)
    Download the emoticon model into checkpoint file
    CUDA_VISIBLE_DEVICE=0 python emotion.py --img ./img/absolute.jpg
``` 
Для валидации одного изображения

<img src="https://github.com/Sergey-Kit/MFDP_Emotion_Recognition/blob/main/img/absolute.jpg" width=30% height=30%>

![image](https://github.com/Sergey-Kit/MFDP_Emotion_Recognition/blob/main/img/power.jpg)

## Результаты

На данном этапе получил Confusion Matrix со приемлимыми метриками после добавления RetinaFace. 
Файл metrics.ipynb с Confusion Matrix

Было:
         ![image](https://github.com/Sergey-Kit/MFDP_Emotion_Recognition/blob/main/img/results.jpg)

Стало с RetinaFace:
![image](https://github.com/Sergey-Kit/MFDP_Emotion_Recognition/blob/main/img/results_v2.jpg)


