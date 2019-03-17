from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=150)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    text = models.TextField()
