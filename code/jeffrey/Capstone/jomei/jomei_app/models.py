from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# class Layer(models.Model):
#     name = models.CharField(max_length = 21)

#     def __str__(self):
#         return self.name

class Point(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Owner')
    name = models.CharField(max_length = 32)
    tag = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    distance_away = models.PositiveIntegerField()
    layer = models.BooleanField(default=False)
    created_date = models.DateTimeField("date_created", auto_now_add=True)
    last_modified_date = models.DateTimeField("last_date_modified", auto_now_add=True)

    def __str__(self):
        return self.name

class UserLocationPoint(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Owner')
    name = models.CharField(max_length = 32)
    tag = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    distance_away = models.PositiveIntegerField()
    layer = models.BooleanField(default=False)
    created_date = models.DateTimeField("date_created", auto_now_add=True)
    last_modified_date = models.DateTimeField("last_date_modified", auto_now_add=True)

    def __str__(self):
        return self.name