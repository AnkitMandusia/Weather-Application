# Django Weather App

## Description

This repository contains a modified version of an open-source Django project. The original project provided a basic backend and frontend setup. I have extended it by adding the following functionalities:

- **Weather History**: An endpoint that allows users to retrieve historical weather data for a specified location.
- **Weather Data Store**: A feature that stores and manages weather data, enabling efficient retrieval and use of past weather information.

The added features demonstrate the use of Django’s MVC architecture and API development capabilities.

## Getting Started

### Prerequisites

- Python 3.8 or later
- Docker
- AWS CLI (optional, for deployment)

### Running the Application Locally

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   
 
2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv env
    source env/bin/activate  

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt

4. **Apply Migrations**

    ```bash
    python manage.py migrate

5. **Run the Development Server**

    ```bash
    python manage.py runserver

The application will be running at http://127.0.0.1:8000/. 

6. **Dockerization**
 

    ```bash
    docker build -t django-weather-app .

7. **Run the Docker Container**

    ```bash
    docker run -d -p 8000:8000 django-weather-app
 
The application will be available at http://localhost:8000/.

Deployment to AWS Lambda
Package the Application

Ensure you have the AWS CLI configured with appropriate permissions. First, create an Amazon Elastic Container Registry (ECR) repository:

    ```bash

    aws ecr create-repository --repository-name                      
    django-weather-app
Tag and push your Docker image to ECR:

    ```bash

    docker tag django-weather-app:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/django-weather-app:latest
    docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/django-weather-app:latest
8. **Create a Lambda Function**

Go to the AWS Lambda console.
Create a new Lambda function.
Choose the “Container image” option and select the image you pushed to ECR.
Configure API Gateway

Go to the API Gateway console.  
Create a new API and configure it to trigger your Lambda function.
Deploy and Test

Deploy the API Gateway.
Test your endpoints using the provided URL.
Note: Due to time constraints, there might be an unresolved error in the deployment. Please refer to the AWS Lambda logs for any issues.