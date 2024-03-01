from django.db import models
from db_connection import db

# Create your models here.

survey_collection = db['survey']
response_collection = db['responses']
user_collection = db['user']