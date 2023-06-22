from django.db import models

class Speakers(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 255)