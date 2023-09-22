from django.urls import path
from . import views

urlpatterns = [
    path(
        'api/lessons/', views.LessonListAPIView.as_view(), name='lesson-list'),
    path(
        'api/products/<int:product_id>/lessons/',
        views.ProductLessonsAPIView.as_view(),
        name='product-lessons'),]