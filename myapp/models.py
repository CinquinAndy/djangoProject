from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    catchphrase = models.CharField(max_length=300)

    def __str__(self):
        return self.name