from django.urls import path
from .views import Author, AuthorByID, Book, BookByID

urlpatterns = [
    path('author/', Author.as_view()),
    path('author/<int:id>/', AuthorByID.as_view()),
    path('book/', Book.as_view()),
    path('book/<int:id>/', BookByID.as_view()),
]

