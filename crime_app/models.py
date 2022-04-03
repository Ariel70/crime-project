from django.db import models


class Crime(models.Model):
    date = models.DateField()
    borough = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    count = models.PositiveIntegerField()
