from django.shortcuts import render, get_object_or_404
from . import models


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
