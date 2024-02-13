from django.shortcuts import render
from .serializers import *
from .models import Author, Book
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import generics
import django_filters
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView



class AuthorListAPIView(APIView):

    def get(self, request):
        queryset = Author.objects.all()
        return JsonResponse(AuthorSerializer(queryset, many=True).data, safe=False)


class BookFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Book
        fields = {'name': ['exact'], 'author': ['exact'], 'pagination_num': ['gte', 'exact', 'gte']}

class BookListAPIView(generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_class = BookFilter


class BaseDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class AuthorDetailApiView(BaseDetail):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookDetailApiView(BaseDetail):

    queryset = Book. objects.all()
    serializer_class = BookSerializer