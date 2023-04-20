from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('generate/', include('generateName.urls')),
<<<<<<< HEAD
    path('estimate/', include('estimateName.urls')),
    # path('pat/', include('patCat.urls')),
    # path('arrange/', include('arrangeTheCats.urls')),
=======
    # path('estimate/', include('estimateName.urls')),
    path('pat/', include('patCat.urls')),
    path('arrange/', include('arrangeTheCats.urls')),
>>>>>>> pat
    path('', include('CetApp.urls')),
]