from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
