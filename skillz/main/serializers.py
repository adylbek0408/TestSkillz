# serializers.py
from rest_framework import serializers
from .models import Course, Article, FreeWorkshops


class ArticleSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name', read_only=True)
    course_id = serializers.IntegerField(source='course.id', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(source='article_course', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class FreeWorkshopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeWorkshops
        fields = '__all__'
