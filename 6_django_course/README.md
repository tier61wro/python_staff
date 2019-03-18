#### 1 общяя инфа ####
курс тут:
https://itproger.com/course/django

Сайт на Django строится из одного или нескольких приложений, которые рекомендуется делать отчуждаемыми и подключаемыми. Это одно из существенных архитектурных отличий этого фреймворка от некоторых других (например, Ruby on Rails). Один из основных принципов фреймворка — DRY (англ. Don't repeat yourself)<br />

Также, в отличие от других фреймворков, обработчики URL в Django конфигурируются явно при помощи регулярных выражений.<br />

Для работы с базой данных Django использует собственный ORM, в котором модель данных описывается классами Python, и по ней генерируется схема базы данных.<br />

WSGI (англ. Web Server Gateway Interface) — стандарт взаимодействия между Python-программой, выполняющейся на стороне сервера, и самим веб-сервером, например Apache.<br />

По стандарту, WSGI-приложение должно удовлетворять следующим требованиям:<br />

должно быть вызываемым (callable) объектом (обычно это функция или метод)<br />
принимать два параметра:<br />
	1.словарь переменных окружения (environ)<br />
	2.обработчик запроса (start_response)<br />
вызывать обработчик запроса с кодом HTTP-ответа и HTTP-заголовками<br />
возвращать итерируемый объект с телом ответа<br />
Простейшим примером WSGI-приложения может служить такая функция-генератор:<br />
````
 def simplest_wsgi_app(environ, start_response):
     start_response('200 OK', [('Content-Type', 'text/plain')])
     yield 'Hello, world!'
````
#### начальная установка ####
```
sudo apt install python3-pip
pip3 install Django

django-admin startproject
python3.5 manage.py migrate #иначе ошибки
python3.5 manage.py runserver # !!! старт самого сервера
```

после установки 
```db.sqlite3 
manage.py - основной конфигурационный скрипт
mysite
ls  mysite/
  __init__.py
  __pycache__
  settings.py # содержит SECRET_KEY, INSTALLED_APPS
  urls.py
  wsgi.py
```суууууууууууууууууууууууууссссссс
#### Создание первого Django приложения ####
Каждое приложение имеет 3 файла:
```
1. файл для работы с базой данных;
2. шаблоны различных страниц или блоков, которые будут отображены на сайте;
3. файл проверяющий адрес ссылки и открывающий нужный HTML шаблон.(urls)
```
Для создания нового приложения необходимо в командной строке прописать команду startapp и назвать как-нибудь приложение. Оно будет добавлено в ваш проект, после чего вы можете связать его с вашим сайтом.
```
.../django/mysite$ python3.5 manage.py startapp webexample
# создалась новая папка по имени нашего приложения:
ls  webexample/
admin.py  apps.py  __init__.py  migrations  models.py  tests.py  views.py
```
Для связи приложений используйте файл settings.py. В нем в списке INSTALLED_APPS добавьте новый элемент, который должен иметь одинаковое название с вашим приложением.
```
# Application definition

INSTALLED_APPS = [
    'webexample'
```
Теперь веб-сайт знает о существовании этого приложения, но мы до сих пор нигде не вызываем приложение. Поэтому, зайдите в файл mysite/urls.py и в нем пропишите новую ссылку, по которой мы будем подключать приложение при переходе по ссылке:
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('webexample/', include ('webexample.urls'),# ищем файл urls в папке webexample

```
идем во webexample/views.py и создаем вью
```python
# Create your views here.
from django.http import Http.Response
def index(request):
	return HttpResponse("<h3>Привет мир!</h3>")
```
потом в webexample/urls
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```
```
запуск:
~/git/learn_python/6_django_course/django/mysite$ python3.5 manage.py runserver
http://127.0.0.1:8000/webexample/
```
Урок #4 - Шаблонизатор Jinja (Дзиндзя)
С давних пор программисты стараются отделить функциональную часть сайта от визуальной. 
Для решения этой проблемы были созданы различные шаблонизаторы, которые выполняют роль отделения одной части сайта от другой. В языке Питон такой шаблонизатор называется Jinja.
