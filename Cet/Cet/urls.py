from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    # path('generate/', include('generateName.urls')),
<<<<<<< HEAD
<<<<<<< HEAD
    # path('estimate/', include('estimateName.urls')),
<<<<<<< HEAD
    path('pat/', include('patCat.urls')),
=======
=======
>>>>>>> generator
=======
<<<<<<< HEAD
=======
    path('generate/', include('generateName.urls')),
>>>>>>> e57e8c5824fb82be21e4bdf6be31b729c6ce138b
    path('estimate/', include('estimateName.urls')),
    path('pat/', include('patCat.urls')),
    path('arrange/', include('arrangeTheCats.urls')),
<<<<<<< HEAD
>>>>>>> pat
=======
    path('pat/', include('patCat.urls')),
    path('arrange/', include('arrangeTheCats.urls')),
>>>>>>> 4d7cadb08f4e015747dc5c20f5ed0c0434491b54
>>>>>>> estimate
=======
>>>>>>> e57e8c5824fb82be21e4bdf6be31b729c6ce138b
    path('', include('CetApp.urls')),
]
