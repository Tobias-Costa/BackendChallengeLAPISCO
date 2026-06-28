from django.urls import path
from .views import Author, AuthorByID

urlpatterns = [
    path('author/', Author.as_view()),
    path('author/<int:id>/', AuthorByID.as_view())
]

