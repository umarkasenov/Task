from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Clothify.views import AllClothifyListView, ManualClothifyListView, FemaleClothifyListView, ChildrenClothifyListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
    path('', include('Hotel.urls')),
    path('', include('registration_and_authorization.urls')),
    path('all_clothify/', AllClothifyListView.as_view()),
    path('menswear/', ManualClothifyListView.as_view()),
    path('female/', FemaleClothifyListView.as_view()),
    path('children/', ChildrenClothifyListView.as_view()),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
