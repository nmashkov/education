# Use an official Python runtime as a parent image
FROM python:3.10-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install poetry and run install dependencies
RUN pip install poetry

RUN poetry config virtualenvs.in-project true

RUN poetry install

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV DB_PATH postgresql://postgres:156628@localhost/mydatabase

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]