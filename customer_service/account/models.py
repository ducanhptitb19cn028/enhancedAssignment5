from django.db import models

# Create your models here.
class Account(models.Model):
    fullname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname