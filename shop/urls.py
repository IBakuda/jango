from django.urls import path
from . import views

urlpatterns = [ # прописываем маршруты для каждого элемента в приложении
    path('', views.index, name='index') # позиционный аргумент, пересылаем из модуля vievs функцию index, после чего даем название пути
]