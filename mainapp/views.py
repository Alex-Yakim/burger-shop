from django.shortcuts import render
from django.views.generic import ListView

from .models import Menu


# Create your views here.

class MenuList(ListView):
    model = Menu
    queryset = Menu.objects.all()
    template_name = 'menu/menu.html'
