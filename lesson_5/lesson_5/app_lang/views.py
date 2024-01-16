from django.shortcuts import render, redirect
from .models import Book
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext
from django.views.decorators.cache import cache_page
from .forms import BookForm
from django.core.cache import cache

CACHE_TIMEOUT = 60
# @cache_page(60)
def books_list(request, *args, **kwargs):

    if request.method == 'GET':
        print(cache.get('books'))
        book_form = BookForm()
        # if cache.get('books') is None:
        #     books = Book.objects.all()
        #     cache.set('books', books, CACHE_TIMEOUT)
        # else:
        #     books = cache.get('books')
        books = cache.get_or_set('books', Book.objects.all(), CACHE_TIMEOUT)
        count = len(books)
        books_num = ngettext(
            'here is %(count)d book',
            'here are %(count)d books',
            count,
        ) % {
            'count': count
        }
        page_title = _('Books')
        return render(request, 'app_lang/index.html', context={'books': books, 'page_title': page_title, 'books_num': books_num, 'book_form': book_form})
    else:
        book = BookForm(request.POST)
        if book.is_valid():
            cache.delete('books')
            book.save()
            return redirect('books')