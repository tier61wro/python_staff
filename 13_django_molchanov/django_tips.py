каждый урок - ветка
мердж ветки
merge remote branch to master
git checkout master
git pull origin master
git merge test
git push origin master
----
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

создание нового приложения с именем blog:
    идем в ~/git/learn_python/13_django_molchanov/app/blogengine
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

запуск сервера:
python3.7 manage.py runserver и_номер_порта
----
урок 2 Роутинг заросов
mvc - паттерн проектирования:

Model - бд
View - демонстрация ответа пользователю - шаблоны на деле
Controller - маршрутизация запросов - views на деле

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
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include("blog.urls"))
]
----
3 урок наслеледование шаблона
создаем папку с шаблонами:
/Users/a.kondrikov/git/learn_python/13_django_molchanov/
app/blogengine/blog/templates/blog
шаблоны размещаются по папкам чтобы избежать конфликтов

передача переменной в шаблон:
#views.py
def posts_list(request):
    n = 'sasha'
    return render(request, 'blog/index.html', context = {'name': n })

#template отображение переданной переменной
<p>{{name}}</p>
процесс наполнения шаблона данными называется рендеринг

#цикл внутри шаблона:
{% for n in names %}
<p>{{n}}</p>
{% endfor %}

создаем базовый шаблон чтобы наследовать остальные от него
подключаем к нему bootstrap для этого идем на
https://getbootstrap.com/docs/4.3/getting-started/introduction/
и копирурем оттуда
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
который вставляем в head шаблона
----
4 урок Модели
ORM - объектно ориентированный мапинг
m-maping - соотношение карты и местности
у нас вместо карты у нас объекты питона - вместо местности база данных
идем в models.py и создаем класс который описывает наш пост:
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)#db_index - для быстрой индексации
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)#CharField - валидатор
    date_pub = models.DateField(auto_now_add=True)

    def __str__(self): # метод класса (модели) отвечает за вывод инф о объекте, мы переопределяем его
        return '{}'.format(self.title) # если принтить объект без этого то будет некрасиво
slug - чпу человекопонятный урл (поле slug уникальное для поста)
#----------- создаем изменнения в базе
чтобы все применилось в бд нам нужно сделать мигрэйт
мигрэйт по сути гит для баз данных
~/git/learn_python/13_django_molchanov/app/blogengine$ ./manage.py makemigrations - создает именения
после этого пояавилась папка
  blog/migrations/0001_initial.py
    - Create model Post
#----------- применяем изменения в базе
~/git/learn_python/13_django_molchanov/app/blogengine$ ./manage.py makemigrations -  применяет именения
(venv) 20:11:05-a.kondrikov@mymac:~/git/learn_python/13_django_molchanov/app/blogengine$ ./manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK
#----------- создание поста руками
# переходим в консоль Джанго и создаем пост руками
~/git/learn_python/13_django_molchanov/app/blogengine$  ./manage.py shell
Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43)
>>> from blog.models import Post
>>> p= Post(title='New post', slug='new-slug', body='new post body')
>>> p
<Post: New post>
>>> p.id
>>> p.title
'New post'
>>> p.slug
'new-slug'
>>> p.save()
>>> p.id
1
>>>
#создали экземпляр вручную -  сохраняем изменения при помощи p.save
#-----------
Джанго при создании объекта прибавляет к нему менеджера оъекта
Он находится в атрибуте objects
все операции чтения и изменения в БД осуществляются через менеджер модели:
#создаем в консоли экземпляр класса пост через менеджер модели
>>> p1 = Post.objects.create(title='new_post', slug='new_slug', body='body')
>>> p1
<Post: new_post>
# выведем на экран все экземпляры используя метод all()
>>> Post.objects.all()
<QuerySet [<Post: New post>, <Post: new_post>]>
# наедем нужный пост при помощи метода get()
>>> post = Post.objects.get(title='New post')
>>> post
<Post: New post>
# по дефолту get регистрозависимый, делаем независимый используя лукап iexact
>>> post = Post.objects.get(slug__iexact='New-slug')
>>> post
<Post: New post>
>>> post = Post.objects.get(slug__iexact='nEw-slug')
>>> post
<Post: New post>
# если больше одного то вместо get filter, лукап для поиска по подстроке - contains
>>> post = Post.objects.filter(slug__contains='slug')
>>> post
<QuerySet [<Post: New post>, <Post: new_post>]>
# iexact, contains это Джанго lookups, ,список тут:
https://docs.djangoproject.com/en/2.2/ref/models/querysets/#field-lookups
# Field lookups are how you specify the meat of an SQL WHERE clause. They’re specified as keyword arguments to the QuerySet methods filter(), exclude() and get().

#------------------ добавляем немного верстки
идем во
https://getbootstrap.com/docs/4.3/components/card/#header-and-footer
и берем оттуда card и запишиваем его в цикл отображения постов

{% for post in posts %}
<div class="card">
    <div class="card-header">
        {{ post.date_pub }}
    </div>
    <div class="card-body">
        <h5 class="card-title">{{ post.title }}</h5>
        <p class="card-text"> {{ post.body|truncatewords:15 }} </p>
        <!--#фильтр для шаблона-->
        <a href="#" class="btn btn-light">Read</a>
    </div>
</div>
<p>{{post.title}}</p>
{% endfor %}
{% endblock %}
# фильтры для шаблонов всегда идут после |
# список фильтров https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#ref-templates-builtins-filters
# описание языка шаьлонов джанго https://docs.djangoproject.com/en/2.2/ref/templates/language/

чтобы сделать незахардкоженные ссылки меняем в шаблоне:
<!--<a class="nav-link" href="/blog">Blog </a>-->
на
<a class="nav-link" href="{% url 'posts_list_url' %}">Blog </a>
#а в urls.py прописываем поле name для урла
#path('', posts_list)
path('', posts_list, name='posts_list_url')

структура шаблонов
/Users/a.kondrikov/git/learn_python/13_django_molchanov/app/blogengine
./templates/base.html
./blog/templates/blog/base_blog.html # только наследование базового
./blog/templates/blog/index.html
./blog/templates/blog/post_detail.html

# index.html для каждого поста
<a href="{% url 'post_detail_url' slug=post.slug %}" class="btn btn-light">Read</a>
# urls.py
path('post/<slug:slug>/', post_detail, name='post_detail_url') # в угловых  скобках именованная группа, слэш в конце обязателен
# views.py
def post_detail(request, slug): # slug прийдет из именованной группы символов 'post/<slug:slug>/'
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post':post})
# хотим себе упростить жизнь тут
#<a href="{% url 'post_detail_url' slug=post.slug %}" class="btn btn-light">Read</a>
#чтобы не хардкодить url
<!--<a href="{% url 'post_detail_url' slug=post.slug %}" class="btn btn-light">Read</a>-->
<a href="{{ post.get_absolute_url }}" class="btn btn-light">Read</a>
# в models.py мы определили функцию:
    def get_absolute_url(self): #имя лучше именно такое, возврашает ссылку на конкретный экземпляр класса Post
        return reverse('post_detail_url', kwargs={'slug':self.slug}) # reverse в .py = url в шаблонах

#---------------------
затем идем во вьюхи и там прикручиваем
берем пременные из модели и говорим отрендери нам шаблон вот с такими переменными взятыми из базы через модель
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

#--------------------
5 урок создаем модель Tag, отношения manytomany

для связи manytomany часто используется дополнительная табличка

№   post_id  tag_id
1      1       1
2      1       2

джанго позволяет обойтись без доп талиц
чтобы создать связь можно просто прописать нужные свойства для одной из таблиц

# еще немного премудростей консоли джанго
# делаем правки вручную
#ctr + l - очистка консоли
#берем значения всех полей одного экземпляра по id

#--------models.py Создаем новую модель
class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return '{}'.format(self.title)

#создаем в моделе post дополнительное поле которое будет связвывать ее с tag
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')  # экземпляр класса ManyToManyField
    #related_name  - обозначает свойство которое появится у экзэмпляров класса Tag
    # posts - главный класс, tag - обслуживаюший
#--------

>>> Post.objects.values().filter(id=1)
<QuerySet [{'id': 1, 'title': 'New post', 'slug': 'new-slug', 'body': 'new post body', 'date_pub': datetime.date(2019, 6, 29)}]>
#берем значения всех полей всех экземпляров класса
>>> Post.objects.values()
<QuerySet [{'id': 1, 'title': 'new_post1', 'slug': 'new-post1', 'body': 'new post body', 'date_pub': datetime.date(2019, 6, 29)}, {'id': 2, 'title': 'new_post2', 'slug': 'new-post2', 'body': 'body', 'date_pub': datetime.date(2019, 6, 29)}, {'id': 3, 'title': 'new_post3', 'slug': 'new-post3', 'body': 'body', 'date_pub': datetime.date(2019, 6, 29)}, {'id': 4, 'title': 'new_post4', 'slug': 'new-post4', 'body': 'body', 'date_pub': datetime.date(2019, 6, 29)}, {'id': 5, 'title': 'new_post5', 'slug': 'new-post5', 'body': 'body', 'date_pub': datetime.date(2019, 6, 29)}]>
# меняем значение поля для экземпляра
>>> post = Post.objects.get(id=1)
>>> post.slug = 'new-post1'
>>> post.save()

#-------------- создаем экземпляр(объект) класса tag
>>> django_t = Tag.objects.create(title='django', slug='django')
>>> django_t
<Tag: django>
#привязываем его:
>>> post.tags.add(django_t)

# ------ делаем тоже самое в джанго
#создаем отдельный шаблон для отображения тегов tags_list.html

{% block content %}
    <h1 class="mt-5">Tags:</h1>

    {% for tag in tags %}
        {{ post.body }}
    <h3 class="mt-5">{{tag.title}}</h3>
    {% endfor %}
{% endblock %}

# views.py создаем вьюху для отображения тегов
def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

# urls.py
path('tags/', tags_list, name='tags_list_url')

# теперь делаем отображение конкретнго тега - по аналогии с постами

# и тут Олег решает что копипастить верстку из одного шаблона в другой это зашквар
#(копипастили cards из index.html в tag_detail.html)
делаем шаблон для карточки с тем чтобы потом подключать его через include
создаем внутри папки с шаблонами: templates/blog/ папку includes, в ней post_cart_template.html
внутри шаблона подключаем его как:
{% include 'blog/includes/post_card_template.html' %}

# создали список тегов по аналогии со списком постов
# подправляем футер для карточек
# в футере прописываем для каждого поста список асоциированных с ним тегов
