from storages.backends.s3boto3 import S3Boto3Storage
from dotenv import load_dotenv
import os

load_dotenv()

class StaticStorage(S3Boto3Storage):
    location = os.getenv('STATICFILES_LOCATION')

class MediaStorage(S3Boto3Storage):
    location = os.getenv('MEDIA')
