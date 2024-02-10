from django.contrib import admin
from .models import Author, Book


class AuthorAmin(admin.ModelAdmin):

    model = Author
    list_display = ['first_name', 'lst_name', 'birthday']

class BookAdmin(admin.ModelAdmin):

    model = Book
    list_display = ['name', 'author', 'publish_date']

admin.site.register(Author, AuthorAmin)
admin.site.register(Book, BookAdmin)