from django.views import generic
from . import models


class AllClothifyListView(generic.ListView):
    template_name = 'clothes_catalog/all_clothify.html'
    context_object_name = 'all_clothify'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


class ManualClothifyListView(generic.ListView):
    template_name = 'clothes_catalog/menswear.html'
    context_object_name = 'menswear'
    model = models.Cloth

    def get_queryset(self, **kwargs):
        return self.model.objects.filter(tag__name="male").order_by('-id')


class FemaleClothifyListView(generic.ListView):
    template_name = 'clothes_catalog/female.html'
    context_object_name = 'female_clothify'
    model = models.Cloth

    def get_queryset(self, **kwargs):
        return self.model.objects.filter(tag__name="female").order_by('-id')


class ChildrenClothifyListView(generic.ListView):
    template_name = 'clothes_catalog/children_clothify.html'
    context_object_name = 'children_clothify'
    model = models.Cloth

    def get_queryset(self, **kwargs):
        return self.model.objects.filter(tag__name="children's").order_by('-id')
