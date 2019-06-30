from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Tag

# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

def post_detail(request, slug): # slag прийдет из именованной группы символов 'post/<slug:slug>/'
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post':post})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

def tag_detail(request, slug): # slag прийдет из именованной группы символов 'post/<slug:slug>/'
    tag = Tag.objects.get(slug__iexact=slug) # slug тут уже локальная переменная
    return render(request, 'blog/tag_detail.html', context={'tag':tag})