from django.urls import path
from .views import AuthorListAPIView, BookListAPIView, BookDetailApiView, AuthorDetailApiView

urlpatterns = [
    path('authors/', AuthorListAPIView.as_view(), name='authors'),
    path('books/', BookListAPIView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailApiView.as_view(), name='detail_book'),
    path('authors/<int:pk>/', AuthorDetailApiView.as_view(), name='detail_author'),
]