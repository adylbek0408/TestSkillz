from django.contrib import admin
from .models import Course, Article, FreeWorkshops


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'price', 'created_date', 'updated_date']
    search_fields = ['name', 'author']
    list_filter = ['created_date', 'updated_date']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['course', 'new_price', 'created_date', 'updated_date']
    list_filter = ['created_date', 'updated_date']


@admin.register(FreeWorkshops)
class FreeWorkshopsAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']
    search_fields = ['name']
    list_filter = ['created_date']
