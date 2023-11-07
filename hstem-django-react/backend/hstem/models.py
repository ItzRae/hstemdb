from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.name