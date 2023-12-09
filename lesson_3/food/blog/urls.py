from django.urls import path
from .views import NewsListView, RegisterNews

urlpatterns = [
    path('news_list/', NewsListView.as_view(), name='news_list'),
    path('new_news/', RegisterNews.as_view(), name='register_news')
]