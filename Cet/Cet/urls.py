from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('generate/', include('generateName.urls')),
<<<<<<< HEAD
    # path('estimate/', include('estimateName.urls')),
<<<<<<< HEAD
    path('pat/', include('patCat.urls')),
=======
=======
<<<<<<< HEAD
    path('estimate/', include('estimateName.urls')),
<<<<<<< HEAD
>>>>>>> estimate
    # path('pat/', include('patCat.urls')),
>>>>>>> b62f4297a0614e958e5fa281040c08a28bee7f28
    # path('arrange/', include('arrangeTheCats.urls')),
=======
    # path('estimate/', include('estimateName.urls')),
    path('pat/', include('patCat.urls')),
    path('arrange/', include('arrangeTheCats.urls')),
>>>>>>> pat
=======
    path('pat/', include('patCat.urls')),
    path('arrange/', include('arrangeTheCats.urls')),
>>>>>>> 4d7cadb08f4e015747dc5c20f5ed0c0434491b54
    path('', include('CetApp.urls')),
]
