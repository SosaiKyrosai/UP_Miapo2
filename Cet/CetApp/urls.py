<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='home'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
=======
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='home'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
>>>>>>> estimate
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)