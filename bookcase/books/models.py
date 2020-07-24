from django.db import models
from users.models import CustomUser


class Book(models.Model):
    author_name = models.CharField(max_length=50)
    author_lastname = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)


class BookcaseCart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)
    borrow_date = models.DateTimeField()
    return_date = models.DateTimeField()
