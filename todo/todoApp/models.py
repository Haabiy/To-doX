from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class todo(models.Model):
    title = models.CharField(max_length = 150)
    content = models.CharField(max_length = 400)
    #date_posted = models.DateTimeField(default=datetime.now, blank=True) # does the same thing but doesn't allow to be updated.
    date_posted = models.DateTimeField(auto_now_add=True)
    #user = models.ForeignKey(User, max_length = 10, on_delete = models.CASCADE, null=True)
    user = models.OneToOneField(User, max_length = 10, on_delete = models.CASCADE, null=True)
    
    # By default, it takes the plural form of the model name: todo -> "todos" on the http://127.0.0.1:8000/admin/ portal (running the server)
    # We can rename by the following if we are not okay taking the plural form of our model name.
    '''class Meta:
        verbose_name_plural = "Todo"'''
    

class Profile(models.Model):
    ProfilePicture = models.ImageField(null=True, blank=True, default='Default.png') # http://127.0.0.1:8000/admin/todoApp/profile/
    user = models.ForeignKey(User, max_length = 10, on_delete = models.CASCADE, null=True)

    
