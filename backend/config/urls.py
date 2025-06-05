from django.contrib import admin
from django.urls import path, include
from .views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  #dev_1
    path('', main, name='main_page'),  # dev_1
]
