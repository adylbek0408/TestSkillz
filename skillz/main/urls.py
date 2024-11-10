from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, ArticleViewSet, FreeWorkshopsViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'freeworkshops', FreeWorkshopsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
