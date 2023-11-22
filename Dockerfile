FROM python:3.8-slim

WORKDIR /usr/src

RUN apt-get update && apt-get install -y git
RUN git clone --depth 1 --branch 8.5.1 https://github.com/wikimedia/pywikibot

WORKDIR /usr/src/pywikibot

RUN pip install -r requirements.txt
RUN pip install .

ENTRYPOINT ["pwb", "scripts/transferbot.py"]
