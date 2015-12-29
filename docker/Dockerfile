FROM debian:jessie

RUN apt-get update && apt-get install -y git \
                                         python-dev \
                                         python-pip \
                                         lib32ncurses5-dev

RUN pip install virtualenv
RUN git clone https://github.com/whitepatrick/trek_blog.git /trek_blog
RUN bash -c "cd /trek_blog && virtualenv prodenv && source /trek_blog/prodenv/bin/activate"
RUN bash -c "pip install -r /trek_blog/requirements.txt"

ENV VIRTUAL_HOST app
ENV VIRTUAL_PORT 8000

COPY prod_gunicorn /trek_blog/
COPY secret.py /trek_blog/trek_blog/
VOLUME /trek_blog
WORKDIR /trek_blog

ENTRYPOINT /trek_blog/prod_gunicorn
