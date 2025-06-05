from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# dev_1
@api_view(['GET'])
def hello_drf_view(request):
    return Response({"message": "Hello, world!"})


