from django.urls import path
from .views import Author, AuthorByID, Book, BookByID

urlpatterns = [
    path('author/', Author.as_view(), name="author_list"),
    path('author/<int:id>/', AuthorByID.as_view(),  name="author_detail"),
    path('book/', Book.as_view(),  name="book_list"),
    path('book/<int:id>/', BookByID.as_view(),  name="book_detail"),
]

