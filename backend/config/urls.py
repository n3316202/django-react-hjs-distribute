from django.contrib import admin
from django.urls import path, include
from .views import main

#dev_12
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  #dev_1
    path('', main, name='main_page'),  # dev_1
]

#dev_12
if settings.DEBUG:
    import debug_toolbar
 
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns