from django.db import models

# Maps to DB Table


class Task(models.Model):
    name = models.CharField(
        # varchar(30) Not NULL
        max_length=30,
        null=False,
    )
    description = models.TextField()

    priority = models.IntegerField()

    age = models.IntegerField()
