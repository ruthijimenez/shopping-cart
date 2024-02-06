# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and SQLAlchemy
RUN pip install Flask
RUN pip install Flask SQLAlchemy

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for database location
ENV SQLALCHEMY_DATABASE_URI sqlite:///shopping_cart.db

# Run app.py when the container launches
CMD ["python", "app.py"]
