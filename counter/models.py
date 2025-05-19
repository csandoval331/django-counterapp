from django.db import models

# Create your models here.
class Counter(models.Model):
    counter = models.IntegerField(default=0)
    
    def __int__(self):
        return self.counter