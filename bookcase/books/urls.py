from django.urls import path
from books.views import ListBookView, CreationBookView, DeleteBookView, UpdateBookView, DetailBookView, BasketListView, \
    SetBookToLoanedView, DeleteFromBasketView, AddOrRemoveFromBasketView, LoanedByUserView, UserGiveBackBookView, \
    GiveBackAllOrSelectedUserBooks

urlpatterns = [
    path('', ListBookView.as_view(), name='home'),
    path('addbook', CreationBookView.as_view(), name='addbook'),
    path('deletebook/<pk>', DeleteBookView.as_view(), name='deletebook'),
    path('updatebook/<pk>', UpdateBookView.as_view(), name='updatebook'),
    path('detailbook/<pk>/', DetailBookView.as_view(), name='detailbook'),
    path('add_to_basket', AddOrRemoveFromBasketView.as_view(), name='addtobasket'),
    path('basketuser:<pk>', BasketListView.as_view(), name='basketlist'),
    path("delete_from_basket", DeleteFromBasketView.as_view(), name='deletefrombasket'),
    path('set_loaned', SetBookToLoanedView.as_view(), name="setloaned"),
    path('userbooks', LoanedByUserView.as_view(), name='userbooks'),
    path('usergivebackbook', UserGiveBackBookView.as_view(), name='usergivebackbook'),
    path('usergivebackallbooks', GiveBackAllOrSelectedUserBooks.as_view(), name='usergivebackmanybooks')
]
