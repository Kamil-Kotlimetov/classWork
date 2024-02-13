from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'lst_name', 'birthday']


class BookSerializer(serializers.ModelSerializer):

    author = serializers.HyperlinkedRelatedField(view_name='detail_author', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'publish_date', 'pagination_num']