from django.db import models
from django.conf import settings

class Quiz(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default="No description")
    image = models.ImageField(upload_to="quiz_images/", null=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    
