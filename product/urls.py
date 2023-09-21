from django.urls import path, include
from rest_framework import routers
from product.views import LessonsViewSet

router = routers.DefaultRouter()
router.register('lessons', LessonsViewSet, basename='lessons')

urlpatterns = [
    path('v1/', include(router.urls))
]