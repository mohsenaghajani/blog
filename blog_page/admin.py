from django.contrib import admin

from blog_page.models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'auther', 'create_time']
