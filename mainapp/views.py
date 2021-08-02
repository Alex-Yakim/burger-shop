from django.shortcuts import render
from django.views.generic import ListView, View

from .models import Menu, ComboMenu, InstragramPhoto, Testimonials, PhotoGallery, VideoOnIndex


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


class AboutView(View):
    def get(self, request):
        template = 'about/about.html'
        gallery = PhotoGallery.objects.all()
        context = {
            'photos': gallery,
            'inst_photo': instragram(),
            'testimonials': testimonials(),
        }
        return render(request, template, context=context)


class IndexView(View):
    def get(self, request):
        template = 'index.html'
        context = {
            'menu': Menu.objects.all()[:4],
            'combo_menu': ComboMenu.objects.all()[:2],
            'inst_photo': instragram(),
            'testimonials': testimonials(),
            'video': VideoOnIndex.objects.all()[0],
        }
        return render(request, template, context=context)
