from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def getListings(request):
    routes=[
        'GET/api',
        'GET/api/rooms',
        'GET/api/rooms/:id'
    ]
    return Response(routes)
    