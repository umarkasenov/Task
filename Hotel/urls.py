from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_list_view, name="hotel_list"),
    path('hotel_detail/<int:id>/', views.hotel_list_detail_view, name="hotel_detail"),
    path('hotel_detail/<int:id>/delete/', views.delete_hotel_view, name="hotel_delete"),
    path('hotel_detail/<int:id>/update/', views.update_hotel_view, name="hotel_update"),
    path('create_hotel/', views.create_hotel_view, name="create_hotel"),
]
