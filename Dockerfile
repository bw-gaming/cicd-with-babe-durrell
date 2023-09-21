# Use an official Node.js runtime as the base image
FROM node:16

# Get the latest version of Playwright
FROM mcr.microsoft.com/playwright:v1.37.1-jammy

# Set the working directory
WORKDIR /app

# Set the environment path to node_modules/.bin
ENV PATH /app/node_modules/.bin:$PATH

# Copy package.json and package-lock.json
COPY package*.json ./

# Get the needed libraries to run Playwright
RUN apt-get update && apt-get -y install libnss3 libatk-bridge2.0-0 libdrm-dev libxkbcommon-dev libgbm-dev libasound-dev libatspi2.0-0 libxshmfence-dev

# Install OpenJDK (Java 11)
RUN apt-get update && apt-get -y install openjdk-11-jdk

# Set the JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

# Install the dependencies in Node environment
RUN npm install

# Copy your project files into the container
COPY . .

# Set the entry point for the container
CMD ["npx", "playwright", "test"]