from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .utils import ObjectDetailMixin

from .models import Post
from .models import Tag

# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

def post_detail(request, slug): # slag прийдет из именованной группы символов 'post/<slug:slug>/'
    post = Post.objects.get(slug__iexact=slug) # slug тут уже локальная переменная
    return render(request, 'blog/post_detail.html', context={'post':post})



def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


# class PostDetail(View):
#     def get(self, request, slug): # переопределяем метод отвечающий за обработку гет запросов
#         # распределение запросов по http методам занимается класс view
#         #post = Post.objects.get(slug__iexact=slug)
#         post = get_object_or_404(Post, slug__iexact=slug)
#         return render(request, 'blog/post_detail.html', context={'post': post})

class PostDetail(ObjectDetailMixin, View):# порядок важен!!!
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'
