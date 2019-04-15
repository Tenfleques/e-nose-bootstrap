FROM maven:3.6.0-jdk-8-alpine

WORKDIR /app

RUN apk add --no-cache git && git clone -b release --single-branch https://github.com/Tenfleques/e-nose-server.git && cd e-nose-server && mvn clean package && cp target/*with-dependencies.jar /app/server

ADD ./resources/elastic-server/config.json /app/config.json
ADD ./resources/elastic-server/scripts/start-server.sh /usr/bin/nose-server.sh

EXPOSE 7070 
CMD ["bash", "/usr/bin/nose-server.sh"]