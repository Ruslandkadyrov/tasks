from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    # Модель продукта.
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="products"
    )


class Lesson(models.Model):
    # Модель урока с полями:
    # название, ссылка на видео, длительность просмотра,
    # продукты
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(
        Product,
        related_name='lessons'
    )
    link_video = models.URLField(max_length=300)
    viewing_duration = models.IntegerField()


class ViewingLesson(models.Model):
    # Модель: просмотрен урок или нет
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="viewinglesson"
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="viewinglesson"
    )
    viewed_duration = models.IntegerField(default=0)
    viewed = models.BooleanField(default=False)

    def viewed_or_not_viewed(self):
        # Метод который определяет просмотрен ли урок или нет
        # Если проомтрен на 80 и более процентов - то он является просмотренным
        viewing_percentage = (
            self.viewed_duration / self.lesson.viewing_duration
        ) * 100
        if viewing_percentage >= 80:
            self.viewed = True
        else:
            self.viewed = False
        self.save()
