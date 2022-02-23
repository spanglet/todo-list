FROM node:lts-alpine

WORKDIR /app

RUN npm create vite@latest

COPY . .

EXPOSE 5002

CMD ["npm", "run", "dev"]
