from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.TextField(max_length=500, null=False)
    post_title = models.CharField(max_length=255, blank=False)
    img = models.ImageField(default=None, upload_to='blogpost_img', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # category

    def __str___(self):
        return self.post_title


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    story = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:20]
