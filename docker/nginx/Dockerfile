FROM debian:jessie

# Set timezone
RUN echo "America/New York" > /etc/timezone \
 && dpkg-reconfigure -f noninteractive tzdata

RUN echo "deb http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list.d/nginx.list
RUN apt-key adv --fetch-keys "http://nginx.org/keys/nginx_signing.key"
RUN apt-get update && apt-get install -y --no-install-recommends nginx \
                                                                 openssl \
                                                                 ca-certificates

RUN rm -rf /srv/www/*

COPY default /etc/nginx/sites-enabled/
COPY nginx.conf /etc/nginx/conf.d/

VOLUME ["/etc/nginx"]
VOLUME ["/srv/www"]

RUN cd /etc/nginx && openssl req -x509 -nodes -days 365 \
                     -subj '/C=US/ST=New York/L=New York/CN=www.20eyes.org' \
                     -newkey rsa:2048 -keyout /etc/nginx/cert.key -out /etc/nginx/cert.crt

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
