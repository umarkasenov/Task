from django.urls import path
from . import views

urlpatterns = [
    path('', views.HotelListView.as_view(), name="hotel_list"),
    path('hotel_detail/<int:id>/', views.HotelDetailView.as_view(), name="hotel_detail"),
    path('hotel_detail/<int:id>/delete/', views.DeleteHotelView.as_view(), name="hotel_delete"),
    path('hotel_detail/<int:id>/update/', views.UpdateHotelView.as_view(), name="hotel_update"),
    path('create_hotel/', views.CreateHotelView.as_view(), name="create_hotel"),
    path('search/', views.SearchView.as_view(), name="search")
]
