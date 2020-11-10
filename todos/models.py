from django.db import models


class Todo(models.Model):
    headline = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    deadline = models.DateTimeField()
    recurring = models.CharField(max_length=10, default="d")

    def __str__(self):
        return self.headline
# Create your models here.
