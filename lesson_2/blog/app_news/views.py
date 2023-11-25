import datetime
from django.shortcuts import render
from django.http import HttpResponse

def news_list(request, *args, **kwargs):
    date = {
        'date_now': datetime.datetime.now(),
        'news_categories': ('Criminal', 'Politics', 'Sports')
    }
    return render(request, 'app_news/index.html', context=date)