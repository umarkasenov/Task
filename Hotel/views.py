from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms


def update_hotel_view(request, id):
    hotel_id = get_object_or_404(models.Hotel, id=id)
    if request.method == 'POST':
        form = forms.HotelForm(request.POST, instance=hotel_id)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Успешно обновлен в БД</h1> <a href='/'>Главная</a>")
    else:
        form = forms.HotelForm(instance=hotel_id)
    return render(request, template_name="hotels/update_hotel.html",
                  context={"form": form, "hotel_id": hotel_id})


def delete_hotel_view(request, id):
    hotel_id = get_object_or_404(models.Hotel, id=id)
    hotel_id.delete()
    return HttpResponse("<h1>Успешно удален из БД</h1> <a href='/'>Главная</a>")


def create_hotel_view(request):
    if request.method == 'POST':
        form = forms.HotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Успешно добавлен в БД</h1> <a href='/'>Главная</a>")
    else:
        form = forms.HotelForm()
    return render(request, template_name="hotels/create_form.html",
                  context={"form": form})


def hotel_list_view(request):
    if request.method == 'GET':
        hotel = models.Hotel.objects.all()
        return render(request, template_name='hotels/hotel_list.html',
                      context={'hotel': hotel})


def hotel_list_detail_view(request, id):
    if request.method == 'GET':
        hotel_id = get_object_or_404(models.Hotel, id=id)
        return render(request, template_name='hotels/hotel_detail.html',
                      context={'hotel_id': hotel_id})
