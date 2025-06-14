from django.db import models
from datetime import datetime

class Quiz(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="quiz/", null=True, blank=True)
