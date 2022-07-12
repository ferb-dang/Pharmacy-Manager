FROM python:3.8-slim

RUN apt-get update && apt-get install -y libpq-dev python-dev gcc


LABEL maintainer="Vua Trò Chơi<thangdv@vmodev.com>"

RUN mkdir /opt/app
WORKDIR /opt/app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . .

# CMD [ "python","./app/main.py" ]
