# Use an official Python runtime as a parent image (python:3.10)
FROM python:3.10-slim

# Set the working directory to /src
WORKDIR /spotiwhat

# Copy the current directory contents into the container at /app
COPY . /spotiwhat

# Upgrade pip
RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME Spotiwhat

# Go to src folder and run the app when the container launches
CMD ["python", "src/app.py"]