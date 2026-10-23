FROM node:20-alpine
WORKDIR /app

COPY /package.json .
RUN npm install

COPY . .
RUN npx tsc javascript/frontend.ts
EXPOSE 3000

CMD ["npm", "start"]