from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('generate/', include('generateName.urls')),
    # path('estimate/', include('estimateName.urls')),
<<<<<<< HEAD
    path('pat/', include('patCat.urls')),
=======
    # path('pat/', include('patCat.urls')),
>>>>>>> b62f4297a0614e958e5fa281040c08a28bee7f28
    # path('arrange/', include('arrangeTheCats.urls')),
    path('', include('CetApp.urls')),
]