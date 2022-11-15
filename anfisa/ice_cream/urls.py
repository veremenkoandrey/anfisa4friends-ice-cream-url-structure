from django.urls import path

from . import views
# Эта строчка обязательна. 
# Без неё namespace работать не будет:
# namespace должен быть объявлен при include и тут, в app_name
app_name = 'ice_cream'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Список мороженого
    path('ice_cream/', views.ice_cream_list, name='ice_cream_list'),
    # Подробная информация о мороженом. Ждем пременную типа int,
    # и будем использовать ее под именем pk
    path(
        'ice_cream/<int:pk>/', views.ice_cream_detail, name='ice_cream_detail'
    ),
]
