# Use the latest Ubuntu image as the base
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip vim

# Set environment variables for aliases
RUN alias python=python3
RUN alias pip=pip3


# Set the working directory
WORKDIR /bingo

COPY ./requirements.txt ./requirements.txt
COPY ./setup.py ./setup.py

# Copy source
COPY ./bingo ./bingo

# Install modules from requirements
RUN pip3 install -r requirements.txt


# Build the Python CLI app
RUN python3 setup.py build

# Install the Python CLI app
RUN python3 setup.py install

# Set the entry point for the container
#CMD [ "/usr/bin/bash", "radio" ]
