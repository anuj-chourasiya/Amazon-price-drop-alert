from django.db import models

class Info(models.Model):
    url=models.TextField()
    email=models.TextField()
