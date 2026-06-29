from django.urls import path
from .views import Author, AuthorByID, Book, BookByID
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('authors/', Author.as_view(), name="author_list"),
    path('authors/<int:id>/', AuthorByID.as_view(),  name="author_detail"),
    path('books/', Book.as_view(),  name="book_list"),
    path('books/<int:id>/', BookByID.as_view(),  name="book_detail"),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

