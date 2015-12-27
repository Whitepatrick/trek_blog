FROM debian:jessie

# Set timezone
RUN echo "America/New York" > /etc/timezone \
 && dpkg-reconfigure -f noninteractive tzdata

RUN echo "deb http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list.d/nginx.list
RUN apt-key adv --fetch-keys "http://nginx.org/keys/nginx_signing.key"

RUN apt-get update && apt-get install -y --no-install-recommends nginx \
                                                                 openssl \
                                                                 ca-certificates

RUN rm -rf /etc/nginx/conf.d/*
RUN rm -rf /srv/www/*

ADD nginx.conf /etc/nginx/conf.d
ADD flaskconfig /etc/nginx/sites-enabled
RUN echo "daemon off;" >> /etc/nginx/conf.d/nginx.conf

VOLUME ["/etc/nginx"]
VOLUME ["/srv/www"]

CMD ["nginx"]

EXPOSE 80
EXPOSE 443
EXPOSE 8000
