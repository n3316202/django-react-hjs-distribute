from django.urls import path,include

from rest_framework import routers
from api.views import category_view
from api.views.hello_view import hello_drf_view

router = routers.DefaultRouter()
router.register("categories", category_view.CategoryViewSet)

#dev_1
#http://127.0.0.1:8000/api/hello/
urlpatterns = [
    path('hello/',hello_drf_view, name='hello-world'),
    path("", include(router.urls)),
]