from django.shortcuts import render
from django.views.generic import ListView

from .models import Menu, ComboMenu, InstragramPhoto, Testimonials


# Create your views here.
def instragram():
    return InstragramPhoto.objects.all()


def testimonials():
    return Testimonials.objects.all()


class MenuList(ListView):
    model = Menu
    queryset = Menu.objects.all()
    template_name = 'menu/menu.html'


def menu_list(request):
    menu = Menu.objects.all()
    combo_menu = ComboMenu.objects.all()
    inst = instragram()
    testim = testimonials()
    context = {
        'menu_list': menu,
        'combo_menu': combo_menu,
        'inst_photo': inst,
        'testimonials': testim,
    }
    return render(request, 'menu/menu.html', context=context)
