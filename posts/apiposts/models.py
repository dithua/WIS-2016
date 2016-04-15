from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



class Posts(models.Model):
    userId = models.ForeignKey(User)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=512)

    def __str__(self):
        return str(self.title)



class Comments(models.Model):
    postId = models.ForeignKey(Posts)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=512)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)

