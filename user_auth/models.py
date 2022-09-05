from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length = 20)
    email = models.EmailField()
    phone_no = models.CharField(max_length = 20)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    password1 = models.CharField(max_length = 20)
    password2 = models.CharField(max_length = 20)
