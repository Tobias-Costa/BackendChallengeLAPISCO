from django.urls import path
from .views import Author, AuthorByID, Book, BookByID

urlpatterns = [
    path('authors/', Author.as_view(), name="author_list"),
    path('authors/<int:id>/', AuthorByID.as_view(),  name="author_detail"),
    path('books/', Book.as_view(),  name="book_list"),
    path('books/<int:id>/', BookByID.as_view(),  name="book_detail"),
]

