from django.db import models

# Create your models here.

class Users(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=255)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.firstname