from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateField(auto_now_add=True)

    def get_absolute_url(self): #имя лучше именно такое, возврашает ссылку на конкретный экземпляр класса Post
        return reverse('post_detail_url', kwargs={'slug':self.slug}) # reverse в .py = url в шаблонах


    def __str__(self): # метод класса (модели) отвечает за вывод инф о объекте, мы переопределяем его
        return '{}'.format(self.title) # если принтить объект без этого то будет некрасиво
        # а с ним так
        #>> > p
        #< Post: New
        #post >
