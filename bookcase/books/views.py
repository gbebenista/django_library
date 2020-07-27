from django.urls import reverse_lazy as _
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from books.forms import CreateBookForm
from books.models import Book


class ListBookView(ListView):
    model = Book
    template_name = 'books/booklist.html'


class CreationBookView(CreateView):
    form_class = CreateBookForm
    success_url = _('bookslist')
    template_name = 'books/createbook.html'


class DeleteBookView(DeleteView):
    model = Book
    success_url = _('bookslist')
    template_name = 'books/deletebook.html'


class UpdateBookView(UpdateView):
    model = Book
    success_url = _('bookslist')
    fields = ['author', 'title', 'publisher', 'tags', ]
    template_name = 'books/updatebook.html'