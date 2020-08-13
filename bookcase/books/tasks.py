from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
import datetime
from celery import shared_task
from books.models import Book


@shared_task(store_results=True)
def add(x, y):
    return x + y


@shared_task(store_results=True)
def count_books():
    return Book.objects.count()


@shared_task(store_results=True, name='send_remainder_to_return_book')
def send_remainder_to_return_book():
    query = Book.objects.filter(loaned_date__lt=datetime.date.today()-datetime.timedelta(days=0))
    for book in query:
        send_mail("Test", "You have to return book {book.title}", "settings.EMAIL_HOST_USER", ["g.bebenista@interia.pl"], fail_silently=False)
    return "success"

