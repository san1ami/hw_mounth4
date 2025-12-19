from django.db import models
from django.contrib.auth.models import User

class Passport(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    series = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
from django.db import models

# Create your models here.
