from django.contrib.auth import views
from django.urls import path
from books.views import ListBookView, CreationBookView, DeleteBookView, UpdateBookView

urlpatterns = [
    path('overview', views.TemplateView.as_view(template_name='books/overview.html'), name='overview'),
    path('bookslist', ListBookView.as_view(), name='bookslist'),
    path('addbook', CreationBookView.as_view(), name='addbook'),
    path('deletebook/<pk>', DeleteBookView.as_view(), name='deletebook'),
    path('updatebook/<pk>', UpdateBookView.as_view(), name='updatebook')
]