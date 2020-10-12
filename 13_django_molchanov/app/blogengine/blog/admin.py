from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_pub')

admin.site.register(Post, PostAdmin)