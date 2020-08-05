from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView, RedirectView
from books.forms import CreateBookForm, UpdateBookForm
from books.models import Book, UserBasket


class ListBookView(ListView):
    model = Book
    template_name = 'books/booklist.html'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            return Book.objects.all().order_by('title')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(publisher__icontains=query)
        )
        return object_list.order_by('title')


class CheckBasketView(RedirectView):
    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            basket = UserBasket.objects.filter(user_id=request.user).first()
            if not basket:
                return JsonResponse({"success": False})
            return JsonResponse({"success": True})
        return JsonResponse({"success": False})


class SendToBasketView(RedirectView):
    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            book = Book.objects.get(id=request.POST.get('book_id'))
            basket = UserBasket.objects.filter(user_id=request.user).first()
            if not basket:
                create_basket = UserBasket.objects.create(user_id=request.user)
                create_basket.books.add(book)
                create_basket.save()
                return JsonResponse({"success": True})
            basket.books.add(book)
            basket.save()
            return JsonResponse({"success": True})
        return JsonResponse({'success': False})


class BasketListView(ListView):
    model = UserBasket
    template_name = 'books/basketlist.html'

    def get_queryset(self):
        basket_list = UserBasket.objects.filter(Q(user_id=self.request.user))
        return basket_list


class DeleteFromBasketView(RedirectView):
    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            book = Book.objects.get(id=request.POST.get('book_id'))
            basket = UserBasket.objects.get(user_id=request.user)
            basket.books.remove(book)
            return JsonResponse({"success": True})
        return JsonResponse({"success": False})


class SetBookToLoanedView(RedirectView):
    def get(self, request, **response_kwargs):
        basket = UserBasket.objects.get(user_id=request.user)
        for b in basket.books.all():
            if b.is_loaned == False:
                book = Book.objects.get(id=b.id)
                book.is_loaned = True
                book.loaner_user = request.user
                book.save()
        basket.delete()
        return redirect("home")


class CreationBookView(CreateView):
    form_class = CreateBookForm
    success_url = reverse_lazy('home')
    template_name = 'books/createbook.html'


class DeleteBookView(DeleteView):
    model = Book
    success_url = reverse_lazy('home')
    template_name = 'books/deletebook.html'


class UpdateBookView(UpdateView):
    model = Book
    form_class = UpdateBookForm
    success_url = reverse_lazy('home')
    template_name = 'books/updatebook.html'


class DetailBookView(DetailView):
    model = Book
    success_url = reverse_lazy('home')
    template_name = 'books/detailbook.html'


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'books/base.html'


class LoanedByUserView(ListView):
    model = Book
    template_name = 'books/userbookslist.html'

    def get_queryset(self):
        book = Book.objects.filter(Q(loaner_user=self.request.user))
        return book


class UserGiveBackBookView(RedirectView):
    def get(self, request, *args, **kwargs):
        if request.is_ajax:
            book = Book.objects.get(id=request.POST.get('book_id'))
            book.is_loaned = False
            book.loaner_user = None
            book.save()
            return JsonResponse({"success": True})
        return JsonResponse({"success": False})