from __future__ import absolute_import, unicode_literals
from celery import shared_task
from books.models import Book


@shared_task
def add(x, y):
    return x + y

@shared_task(store_results=True)
def count_books():
    return Book.objects.count()
