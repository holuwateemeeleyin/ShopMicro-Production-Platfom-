# Stage 1: Build
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install --omit=dev

# Stage 2: Production
FROM node:20-alpine
WORKDIR /app
# 1. Copy dependencies
COPY --from=builder /app/node_modules ./node_modules
# 2. Copy EVERYTHING from your local backend folder to /app
COPY . . 

# Verify the file exists during build (DevOps trick)
RUN ls -l /app/server.js

USER node
EXPOSE 8080
CMD ["node", "server.js"]