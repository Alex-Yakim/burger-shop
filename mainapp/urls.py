from django.urls import path
from . import views

urlpatterns = [
    # path('menu/', views.MenuList.as_view(), name='menu')
    path('menu/', views.menu_list, name='menu')
]