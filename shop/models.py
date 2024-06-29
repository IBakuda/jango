from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model): # создание категорий курсов
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self): # В надмин панели будет выводится название категории
        return self.title

class Course(models.Model): # создание курсов
    title = models.CharField(max_length=300)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # Если удалить категорию, то афтоматически удалится курс входящий в категорию
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self): # В надмин панели будет выводится название курса
        return self.title