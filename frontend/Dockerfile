# FROM node:18.18.0-alpine as build
# WORKDIR /app
# COPY package*.json ./
# RUN npm install
# COPY . ./
# RUN npm run build
# CMD cp -r build result_build


FROM node:18
WORKDIR /app
COPY frontend/package*.json ./frontend/
WORKDIR /app/frontend
RUN npm install
WORKDIR /app
COPY frontend/ ./frontend/
EXPOSE 5173
CMD ["npm", "start"]
