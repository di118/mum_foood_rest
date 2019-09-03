# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7-alpine

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /code

# Set the working directory to /code
WORKDIR /mum_food_rest
COPY . /mum_food_rest/
# Copy the current directory contents into the container at /code


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt