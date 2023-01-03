from django.db import models

# Create your models here.
#create a user model
class User(models.Model):
    uid = models.CharField('User ID',max_length=255)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name