from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app.views import (IndexPageView, PetListView, PetView, CatListView, DogListView, ParrotListView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PetListView.as_view()),
    path('cats/', CatListView.as_view()),
    path('dogs/', DogListView.as_view()),
    path('parrots/', ParrotListView.as_view()),
    path('pets/<str:pk>/', PetView.as_view()),
    path('about_us/', IndexPageView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
