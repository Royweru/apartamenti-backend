from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ListingSerializer
from .models import Listing
# Create your views here.

@api_view(['GET','POST'])
def api_Listings(request):
    if request.method == 'GET':
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings,many=True)
        return Response(serializer.data)
    
    if request.method =='POST':
        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET','PUT'])
def individual_Listing(request,pk):
    listing = Listing.objects.get(id=pk)
    if request.method=='GET':
        serializer = ListingSerializer(listing,many=False)
        return Response(serializer.data)
        
     
    if request.method=="PUT":
        serializer = ListingSerializer(listing,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
   

 
