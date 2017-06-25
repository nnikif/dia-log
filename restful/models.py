from django.db import models
from django.utils import timezone
# Create your models here.


class Dialogue (models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)