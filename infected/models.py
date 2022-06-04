from django.db import models

class sick(models.Model):
    name = models.TextField(blank=True)
    ability = models.TextField()
