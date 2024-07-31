import os
import sys
from django.core.wsgi import get_wsgi_application

# Ensure the settings module is set correctly
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_proj.settings')

# Add the project directory to the system path
sys.path.append('/app')

# Create the WSGI application
application = get_wsgi_application()

# Define the Lambda handler function
def handler(event, context):
    from mangum import Mangum
    asgi_handler = Mangum(application)
    response = asgi_handler(event, context)
    return response
