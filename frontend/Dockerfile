FROM node:20-alpine
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
# Vite needs to be told to listen on all interfaces to work in Docker
EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]