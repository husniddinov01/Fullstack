from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    # class Meta:


    def __str__(self):
        return self.username



class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

