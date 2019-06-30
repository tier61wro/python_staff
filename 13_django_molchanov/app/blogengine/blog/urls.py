from django.urls import path

from .views import *

urlpatterns = [
    #path('', posts_list)
    path('', posts_list, name='posts_list_url'),
    path('post/<slug:slug>/', post_detail, name='post_detail_url') # в угловых  скобках именованная группа, слэш в конце обязателен
]