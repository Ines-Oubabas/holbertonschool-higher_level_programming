# Use the Alpine base image
FROM alpine:latest

# Install the curl package
RUN apk add --no-cache curl

# Copy the config.txt file to the /app directory in the container
COPY config.txt /app/config.txt

# Set the working directory
WORKDIR /app
