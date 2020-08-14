from __future__ import absolute_import, unicode_literals
from django.core.mail import EmailMultiAlternatives
import datetime
from celery import shared_task
from books.models import Book
from django.template.loader import get_template


@shared_task(store_results=True, name='send_remainder_to_return_book')
def send_remainder_to_return_book():
    query = Book.objects.filter(loaned_date__lte=datetime.date.today() - datetime.timedelta(days=30))
    subject, from_email, to = "Reminder to return book", "settings.EMAIL_HOST_USER", ["g.bebenista@interia.pl"]
    html_template = get_template('books/email.html')
    for book in query:
        context = {'book_id': book.id, 'book_title': book.title}
        html_content = html_template.render(context)
        email = EmailMultiAlternatives(subject=subject, from_email=from_email, to=to)
        email.attach_alternative(html_content, "text/html")
        email.send()
    return "success"
