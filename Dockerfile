FROM python:2

WORKDIR /usr/src/app

COPY ./startup.sh ./
COPY ./run.py ./

RUN pip install requests beautifulsoup4
RUN ["chmod", "+x", "./startup.sh"]

CMD ./startup.sh
