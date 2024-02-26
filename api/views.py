from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ListingSerializer
from .models import Listing
# Create your views here.

@api_view(['GET'])
def getListings(request):
    listings = Listing.objects.all()
    serializer = ListingSerializer(listings,many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def getListing(request,pk):
    listing = Listing.objects.get(id=pk)
    images = listing.image_set.all()
    serializer = ListingSerializer(listing,many=False)
    return Response(serializer.data)

