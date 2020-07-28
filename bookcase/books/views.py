from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView

from books.forms import CreateBookForm
from books.models import Book


class ListBookView(ListView):
    model = Book
    template_name = 'books/booklist.html'
    paginate_by = 5


class CreationBookView(CreateView):
    form_class = CreateBookForm
    success_url = reverse_lazy('bookslist')
    template_name = 'books/createbook.html'


class DeleteBookView(DeleteView):
    model = Book
    success_url = reverse_lazy('bookslist')
    template_name = 'books/deletebook.html'


class UpdateBookView(UpdateView):
    model = Book
    success_url = reverse_lazy('bookslist')
    fields = ['author', 'title', 'publisher', 'tags', ]
    template_name = 'books/updatebook.html'


class SearchBookView(ListView):
    model = Book
    fields = ['author', 'title', 'publisher', 'tags', ]
    template_name = 'books/booklist.html'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains=query)
        )
        return object_list


class DetailBookView(DetailView):
    model = Book
    success_url = reverse_lazy('bookslist')
    template_name = 'books/detailbook.html'


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'books/base.html'
