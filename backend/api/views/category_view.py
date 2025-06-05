from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Category
from api.serializers.category_serializer import CategorySimpleSerializer
from rest_framework.viewsets import ModelViewSet


# dev_1
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySimpleSerializer


