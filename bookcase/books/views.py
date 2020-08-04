from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView

from books.forms import CreateBookForm, UpdateBookForm
from books.models import Book, UserBasket
from users.models import CustomUser


class ListBookView(ListView):
    model = Book
    template_name = 'books/booklist.html'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            return Book.objects.all().order_by('title')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(publisher__icontains=query) | Q(
                tags__name__icontains=query)
        )
        return object_list.order_by('title')


# class AddCartView(View):
#     model = Book

def send_to_basket(request):
    b = Book.objects.get(id=request.POST.get('book_id'))
    basket = UserBasket.objects.filter(user_id=request.user).first()
    if not basket:
        create_basket = UserBasket.objects.create(user_id=request.user)
        create_basket.books.add(b)
        create_basket.save()
        return JsonResponse({"success": True})
    basket.books.add(b)
    basket.save()
    return JsonResponse({"success": True})


class BasketListView(ListView):
    model = UserBasket
    template_name = 'books/basketlist.html'

    def get_queryset(self):
        basket_list = UserBasket.objects.filter(Q(user_id=self.request.user))
        return basket_list


def delete_from_basket(request):
    b = Book.objects.get(id=request.POST.get('book_id'))
    basket = UserBasket.objects.get(user_id=request.user)
    basket.books.remove(b)
    return JsonResponse({"success": True})


def set_book_to_loaned(request):
    basket = UserBasket.objects.get(user_id=request.user)


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
    form_class = UpdateBookForm
    success_url = reverse_lazy('bookslist')
    template_name = 'books/updatebook.html'


class DetailBookView(DetailView):
    model = Book
    success_url = reverse_lazy('bookslist')
    template_name = 'books/detailbook.html'


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'books/base.html'
