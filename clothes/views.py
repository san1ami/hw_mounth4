from django.views.generic import ListView
from .models import Clothes

class MaleClothesView(ListView):
    template_name = 'clothes/male.html'
    model = Clothes

    def get_queryset(self):
        return Clothes.objects.filter(category__name='Мужская')


class FemaleClothesView(ListView):
    template_name = 'clothes/female.html'
    model = Clothes

    def get_queryset(self):
        return Clothes.objects.filter(category__name='Женская')


class ChildClothesView(ListView):
    template_name = 'clothes/child.html'
    model = Clothes

    def get_queryset(self):
        return Clothes.objects.filter(category__name='Детская')
