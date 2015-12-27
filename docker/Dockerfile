FROM debian:jessie

RUN apt-get update && apt-get install -y git \
                                         python-dev \
                                         python-pip \
                                         lib32ncurses5-dev

RUN git clone https://github.com/whitepatrick/trek_blog.git /trek_blog
RUN bash -c "pip install -r /trek_blog/requirements.txt"

VOLUME /trek_blog
WORKDIR /trek_blog

CMD bash -c "gunicorn -b 0.0.0.0:5000 trek_blog:app"
