FROM node:8-alpine
ADD ./app/ /home/node/app
ADD ./models/ /home/node/models
RUN chown -R node:node /home/node/app
RUN chown -R node:node /home/node/models