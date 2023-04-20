from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate/', include('generateName.urls')),
    path('estimate/', include('estimateName.urls')),
    path('pat/', include('patCat.urls')),
    path('arrange/', include('arrangeTheCats.urls')),
    path('', include('CetApp.urls')),
]
