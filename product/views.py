from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from models import Lesson, Access, LessonView
from serializers import LessonSerializer, LessonViewSerializer


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        accessible_products = Access.objects.filter(user=user).values_list(
            'product_id', flat=True)
        return Lesson.objects.filter(product_id__in=accessible_products)


class ProductLessonsAPIView(generics.ListAPIView):
    serializer_class = LessonViewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        return LessonView.objects.filter(
            user=user, lesson__product_id=product_id)
