from django.urls import path
from . import views

urlpatterns = [
    # path('menu/', views.MenuList.as_view(), name='menu')
    path('menu/', views.menu_list, name='menu'),
    path('about/', views.AboutView.as_view(), name='about')
]