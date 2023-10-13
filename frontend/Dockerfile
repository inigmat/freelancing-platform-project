FROM node:18.18.0-alpine
RUN mkdir /app
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . ./
RUN npm run build
# CMD cp -r . result_build


# FROM node:18.18.0-alpine as build
# WORKDIR /app
# COPY package*.json ./
# RUN npm install
# COPY . ./
# RUN npm run build
# CMD [ "npm", "start" ]