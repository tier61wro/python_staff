
virtualenv venv
source venv/bin/activate

cd app
django-admin startproject blogengine

(venv) 00:06:32-a.kondrikov@mymac:~/git/learn_python/13_django_molchanov/app$ tree
.
└── blogengine
    ├── blogengine
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py

    проект состоит из приложений (apps)
    каждый app по сути папка с файлами

    создание приложения:
    идем в
    ~/git/learn_python/13_django_molchanov/app/blogengine
    и запускаем:
    python3.7 manage.py startapp blog

    tree
.
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

1 directory, 7 files

mvc - паттерн проектирования
model - бд
view - демонстрация ответа пользователю - шаблоны на деле
controller - маршрутизация запросов -views на деле

запуск сервера
python3.7 manage.py runserver

3 урок насделедование шаблона

4 урок
ORM
m-maping
идем в models.py и делаем класс который описывает наш пост
чпу человекопонятный урл (поле слаг уникальное для поста)
для класса описываем поля
чтобы все примеилось в бд нам нужно сделать мигрэйт

manage.py makeingrations - создает именения
manage.py mmigrate -  применяет именения
создаем экзэмпляр вручную -  сохраняем изменения при помощи p.save

затем идем во вьюхи и там прикручиваем
берем пременные из модели и говорим отрендери нам шаблон вот с такими переменными вщятыми из базы через модель
пути динамические
#в urls.py:
path('post/<str:slug>', post_detail, name='post_detail')
в угловых скабках именованная группа
#в views.py
def post_detail(request, slug): - slug = slug!
  post = Post.objects.get(slug_iexact=slug)
  return render(request, 'blog/post_detail.html')
#post_detail.html -  шаблон
{% extends 'blog/base_blog.html' %}

{% block title %}
     {{ post.title }} - {{ block.super }} #наследование из родительского шаблона
{% endblock %}

{% block content %}
    <h1 class="mt-5">
    </h1>
{% endblock %}

url reversing
