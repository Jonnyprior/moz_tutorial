from django.urls import path
from . import views

 # name used to uniquely indentify this URL. Can be used to reverse mapper. For example link pages to home using <a href="{% url 'index' %}">Home</a>
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]
