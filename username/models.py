from django.db import models

# Create your models here.

class Username(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username