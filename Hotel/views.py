from django.shortcuts import get_object_or_404
from django.views import generic
from . import models, forms

# Обновление
class UpdateHotelView(generic.UpdateView):
    template_name = 'hotels/update_hotel.html'
    context_object_name = 'hotel_id'
    form_class = forms.HotelForm
    success_url = "/"

    def get_object(self, **kwargs):
        hotel_id = self.kwargs.get("id")
        return get_object_or_404(models.Hotel, id=hotel_id)

    def form_valid(self, form):
        return super(UpdateHotelView, self).form_valid(form=form)

# Удаление
class DeleteHotelView(generic.DeleteView):
    template_name = 'hotels/delete_hotel.html'
    success_url = "/"

    def get_object(self, **kwargs):
        hotel_id = self.kwargs.get("id")
        return get_object_or_404(models.Hotel, id=hotel_id)

# Создание
class CreateHotelView(generic.CreateView):
    template_name = 'hotels/create_form.html'
    form_class = forms.HotelForm
    success_url = "/"

    def form_valid(self, form):
        return super(CreateHotelView, self).form_valid(form=form)

# Главная
class HotelListView(generic.ListView):
    template_name = "hotels/hotel_list.html"
    context_object_name = "hotel"
    model = models.Hotel

    def get_queryset(self):
        return self.model.objects.all()

# Информация
class HotelDetailView(generic.DetailView):
    template_name = "hotels/hotel_detail.html"
    context_object_name = "hotel_id"

    def get_object(self, **kwargs):
        hotel_id = self.kwargs.get("id")
        return get_object_or_404(models.Hotel, id=hotel_id)

#Поиск


class SearchView(generic.ListView):
    template_name = "hotels/hotel_list.html"
    context_object_name = "hotel"
    paginate_by = 5

    def get_queryset(self):
        return models.Hotel.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context
