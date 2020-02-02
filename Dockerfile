FROM python:2

WORKDIR /usr/src/app

COPY ./startup.sh ./
COPY ./ModemScraper/run.py ./

RUN pip install requests beautifulsoup4
RUN ["chmod", "+x", "./startup.sh"]

CMD ./startup.sh