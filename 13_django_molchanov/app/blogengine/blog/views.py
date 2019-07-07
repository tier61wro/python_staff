from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .utils import ObjectDetailMixin
from django.shortcuts import redirect

from .models import Post
from .models import Tag

from .forms import TagForm

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

class TagCreate(View): # реагирует на гет запрос и на пост запрос - поэтому две функции
    # 1.  задача - get  отображает пользователю нашу форму
    # 2.  post - пользователь ввел данные мы их принимаем и делаем пост запрос
    def get(self, request):
        form = TagForm()
        print (f"FORM = {form}\n")
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request): # 1)создаем экземпляр класса tagform 2)валидируем 3)передаем данные
        #print(dir(request))
        #print(request.POST)
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context= {'form': bound_form}) # если ошибка


