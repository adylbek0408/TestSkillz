from rest_framework import viewsets
from .models import Course, Article, FreeWorkshops
from .serializers import CourseSerializer, ArticleSerializer, FreeWorkshopsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class FreeWorkshopsViewSet(viewsets.ModelViewSet):
    queryset = FreeWorkshops.objects.all()
    serializer_class = FreeWorkshopsSerializer
