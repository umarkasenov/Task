from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_list_view, name="hotel_list"),
    path('hotel_detail/<int:id>/', views.hotel_list_detail_view, name="hotel_detail"),
]
