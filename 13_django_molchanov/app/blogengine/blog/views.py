from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def posts_list(request):
    #return HttpResponse("<h1>Hello from post list</h1>")
    names = ['sasha', 'karo', 'luna']
    return render(request, 'blog/index.html', context={'names': names})
    #return render(request, 'blog/base.html', context={'names': names})
