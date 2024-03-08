from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)  # Определяет модель для тега (например, "платья", "рубашки", "аксессуары" и т. д.)

    def __str__(self):
        return self.name  # Возвращает строковое представление имени тега


class Cloth(models.Model):
    title = models.CharField(max_length=100)  # Определяет модель для одежды с наименованием (например, "Платье в полоску")
    price = models.FloatField(default=100)  # Определяет цену по умолчанию для одежды
    tag = models.ManyToManyField(Tag)  # Связывает множество тегов с одеждой, позволяя одежде иметь несколько тегов

    def __str__(self):
        return self.title  # Возвращает строковое представление имени одежды
