урок 1
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
    ~/git/learn_python/
    13_django_molchanov/app/blogengine
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

запуск сервера
python3.7 manage.py runserver и_номер_порта
----
урок 2 Роутинг заросов
mvc - паттерн проектирования:

Model - бд
View - демонстрация ответа пользователю - шаблоны на деле
Controller - маршрутизация запросов -views на деле

юзаем sqlite

#vievs.py - обработчик запроса браузера всегда на вход принимает
объект request
def hello(request):
    pass

Встроенная функция dir() возвращает отсортированный список строк, содержащих имена, определенные в модуле.
Список содержит имена всех модули, переменных и функций, определенные в модуле.
чтобы приложение заработало добавляем его в settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]

path('blog/', hello, имя, параметры для функции)
подключаем роутинг заросов
path('blog/', include("blog.urls"))
----
3 урок насделедование шаблона

----
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
в угловых скобках именованная группа
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

url reversing - процесс генерации ссылки на объект -  в шаблонах это функция url
а в питоновских файлах reverse
def get_absolute_url(self):
    return reverse('pist_detail_url', kwargs={'slug':self.slug})

в шаблоне:
        <a href="{url 'post_detail_url' slug=post.slug %}"class="btn btn-light">Read</a>"
        меняем на post.get_absolute_url
