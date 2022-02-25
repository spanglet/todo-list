FROM node:lts-alpine

WORKDIR /app

RUN npm create vite@latest

COPY . .

RUN npm install

EXPOSE 3000

CMD ["npm", "run", "dev"]
