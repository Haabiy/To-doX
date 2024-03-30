**Setting up Django with Amazon S3, Amazon RDS, and Amazon Redshift for Static and Media Files**

---

**1. Install Required Packages**

Make sure to include `django-storages` in your `INSTALLED_APPS` within your Django project's `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todoApp',
    "crispy_forms",
    "crispy_bootstrap5",
    "storages",
]
```

You can install `django-storages` via pip:

```bash
pip install django-storages
```
Make sure to install dependencies listed in requirements.txt

```bash
pip3 install -r requirements.txt
```
**2. Configure Amazon S3 Settings**

Set up your Amazon S3 credentials and bucket details in your Django project's `settings.py`:

```python
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')
STATICFILES_LOCATION = os.getenv('STATICFILES_LOCATION')
MEDIAFILES_LOCATION = os.getenv('MEDIA')

AWS_S3_URL_PROTOCOL = 'https'
AWS_S3_USE_SSL = True
AWS_S3_VERIFY = True
AWS_S3_FILE_OVERWRITE = False
```

**3. Configure Storage Backend**

Define custom storage backends for static and media files by creating `s3_storage.py` within your app directory (`todoApp/`), and configure them to point to the desired locations within your S3 bucket:

```python
# todoApp/s3_storage.py

from storages.backends.s3boto3 import S3Boto3Storage
from dotenv import load_dotenv
import os

load_dotenv()

class StaticStorage(S3Boto3Storage):
    location = os.getenv('STATICFILES_LOCATION')

class MediaStorage(S3Boto3Storage):
    location = os.getenv('MEDIA')
```

**4. Set Storage Backends in Django Settings**

Update your `STATICFILES_STORAGE` and `DEFAULT_FILE_STORAGE` settings to use the custom storage backends:

```python
STATICFILES_STORAGE = 'todoApp.s3_storage.StaticStorage'
DEFAULT_FILE_STORAGE = 'todoApp.s3_storage.MediaStorage'
```

**5. Configure Database Settings**

Define the media URL to point to the correct location within your S3 bucket:

```python
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{MEDIAFILES_LOCATION}/'
```

**6. Configure Media URL**

If you are using `Amazon RDS` or `Amazon Redshift` for your database, configure the database settings accordingly in your Django project's settings.py. Update the `DATABASES` dictionary with your database connection details.

**7. Collect Static Files**

Finally, run the following command to collect and upload static files to your S3 bucket:

```bash
python3 manage.py collectstatic
```

---