FROM python:3.8-slim

WORKDIR /usr/src

RUN apt-get update && \
    apt-get install --no-install-recommends -y git=1:2.39.2-1.1 && \
    rm -rf /var/lib/apt/lists/*
RUN git clone --depth 1 --branch 8.5.1 https://github.com/wikimedia/pywikibot

WORKDIR /usr/src/pywikibot

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir .

COPY source_family.py target_family.py ./families/
COPY user-config.py .

ENTRYPOINT ["pwb", "scripts/transferbot.py"]
