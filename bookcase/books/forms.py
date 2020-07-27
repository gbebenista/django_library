from django.forms import ModelForm
from books.models import Book


class CreateBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'publisher', 'tags', ]
