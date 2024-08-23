# Use an official Python runtime as a parent image
FROM python:3.9-slim

RUN apt-get -y update; apt-get -y install curl

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY ./src/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY ./src/ /app

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run streamlit when the container launches
CMD ["streamlit", "run", "main.py"]