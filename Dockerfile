FROM python:3.7

RUN apt-get update && apt-get install -y libgl1-mesa-glx

COPY ./requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

WORKDIR /root
RUN mkdir /.deepface
RUN mkdir /.deepface/weights
COPY ./.deepface/weights ./.deepface/weights
ADD ./checkpoint ./checkpoint
COPY ./functions.py ./functions.py
COPY ./emotion.py ./emotion.py
COPY ./bot.py ./bot.py
COPY ./TG_imgs ./TG_imgs

ENTRYPOINT ["python", "bot.py"]