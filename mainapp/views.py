from django.shortcuts import render
from django.views.generic import ListView

from .models import Menu, ComboMenu


# Create your views here.

class MenuList(ListView):
    model = Menu
    queryset = Menu.objects.all()
    template_name = 'menu/menu.html'


def menu_list(request):
    menu = Menu.objects.all()
    combo_menu = ComboMenu.objects.all()
    return render(request, 'menu/menu.html', context={'menu_list': menu, 'combo_menu': combo_menu})
