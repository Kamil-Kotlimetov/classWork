from django.urls import path
from .views import NewsListView, RegisterNews, NewsDetailView

urlpatterns = [
    path('news_list/', NewsListView.as_view(), name='news_list'),
    path('new_news/', RegisterNews.as_view(), name='register_news'),
    path('news_list/<int:pk>/', NewsDetailView.as_view(), name='news_detail')
]