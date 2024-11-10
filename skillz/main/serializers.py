# serializers.py
from rest_framework import serializers
from .models import Course, Article, FreeWorkshops


class ArticleSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name', read_only=True)
    course_id = serializers.IntegerField(source='course.id', read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'course', 'course_name', 'course_id', 'new_price', 'created_date', 'updated_date']


class CourseSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(source='article_course', many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'author', 'price', 'image', 'description', 'city', 'created_date', 'updated_date',
                  'articles']


class FreeWorkshopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeWorkshops
        fields = ['id', 'name', 'description', 'created_date']
