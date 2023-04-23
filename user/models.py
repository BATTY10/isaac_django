from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    image = models.ImageField(default=None, upload_to='profile_picture')
    address = models.CharField(max_length=255, null=True)
    bio=models.TextField()
    dob = models.DateTimeField()
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
