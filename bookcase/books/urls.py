from django.urls import path
from books.views import ListBookView, CreationBookView, DeleteBookView, UpdateBookView, DetailBookView

urlpatterns = [
    path('', ListBookView.as_view(), name='bookslist'),
    path('addbook', CreationBookView.as_view(), name='addbook'),
    path('deletebook/<pk>', DeleteBookView.as_view(), name='deletebook'),
    path('updatebook/<pk>', UpdateBookView.as_view(), name='updatebook'),
    path('detailbook/<pk>', DetailBookView.as_view(), name='detailbook')
]