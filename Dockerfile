# Use the AWS Lambda Python runtime as a parent image
FROM public.ecr.aws/lambda/python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Django project code into the container
COPY . .

# Ensure the Django settings module is set correctly
ENV DJANGO_SETTINGS_MODULE=weather_proj.settings

# Command to run the Lambda function
CMD ["app.handler"]
