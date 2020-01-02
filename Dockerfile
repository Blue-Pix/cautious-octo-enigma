FROM python:3.6.5-jessie

RUN apt-get update && apt-get install -y \
        mecab \
        libmecab-dev \
        mecab-ipadic \
        mecab-ipadic-utf8 \
        nkf \
        vim \
        sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN cd /usr/local/src/ \
    && git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && cd mecab-ipadic-neologd \
    && ./bin/install-mecab-ipadic-neologd -n -y

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
