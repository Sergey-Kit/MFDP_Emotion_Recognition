# MFDP "Определение эмоций клиента казино"

Для погружения в тему была использованная предобученая NN ResNet18. 
Эту обученную модель для определения 7 эмоций на лицах взял тут (https://github.com/WIKI2020/FacePose_pytorch). 
Датасет EmotioNet (http://cbcsl.ece.ohio-state.edu/EmotionNetChallenge/) с размеченными эмоциями. На нем провалидировал вышеупомянутую модель.

## Demo
```
    # install requirements
    First install Anaconda3, python 3.7,and then:
    pip install numpy opencv-python 
    pip install torch==1.4.0
    pip install torchvision==0.5.0
    Download the emoticon model (the angle model is already in the code):
    [https://pan.baidu.com/s/1oxznkRcP5w8lzYMAjj87-w],accesscode:WIKI
    
    # run the simple inference script(emotion_loop)
    Download the emoticon model into checkpoint file
    CUDA_VISIBLE_DEVICE=0 python emotion_loop.py
```   
Потоком сохраняются изображения из интернета и валидируются моделью. Результат сохраняется в Excel-файл.

## Ркзультаты

На данном этапе получил Confusion Matrix со слабыми метриками. Файл metrics.ipynb

![image](https://github.com/Sergey-Kit/MFDP_Emotion_Recognition/blob/main/img/results.jpg)

Следующим этапом будет преобработка фото. Вырезание лица, удаление лишних данных с фото.
