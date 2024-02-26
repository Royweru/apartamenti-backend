from rest_framework.serializers import ModelSerializer
from .models import Listing,Category,Image

class ListingSerializer(ModelSerializer):
    class Meta:
        model=Listing
        fields='__all__'