from django.contrib import admin
from booktest import models


# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content', 'gender', 'book']


admin.site.register(models.BookInfo, BookInfoAdmin)
admin.site.register(models.HeroInfo, HeroInfoAdmin)
