from django.urls import path

from .views import *

urlpatterns = [
    #path('', posts_list)
    path('', posts_list, name='posts_list_url'),
    #path('post/<str:slug>/', post_detail, name='post_detail_url'), # в угловых  скобках именованная группа, слэш в конце обязателен
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>', TagDetail.as_view(), name='tag_detail_url')
]