# Use official Python image as the base image
FROM python:3.12

# Set working directory in the container
WORKDIR /code

# Copy the requirements file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code to the working directory
COPY . .

# CD into the directory where manage.py is
WORKDIR /code/todo/

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
