from django.db import models
from taggit.managers import TaggableManager
from users.models import CustomUser


class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    tags = TaggableManager()

class BookcaseCart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)
