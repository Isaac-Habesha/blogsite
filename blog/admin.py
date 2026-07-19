from django.contrib import admin
from . import models

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','content','isPublished','number_of_views','created_at')
    list_filter = ('isPublished','created_at','title')
admin.site.register(models.Blog, BlogAdmin)