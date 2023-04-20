from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('generate/', include('generateName.urls')),
    path('', include('CetApp.urls')),
]