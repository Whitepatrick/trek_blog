FROM debian:jessie

RUN apt-get update && apt-get install -y git \
                                         python-dev \
                                         python-pip \
                                         lib32ncurses5-dev

RUN git clone https://github.com/whitepatrick/trek_blog.git /trek_blog
RUN bash -c "pip install -r /trek_blog/requirements.txt"

COPY gunicorn_start /trek_blog
VOLUME /trek_blog
WORKDIR /trek_blog

CMD ["gunicorn_start"]
