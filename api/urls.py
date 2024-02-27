from django.urls import path,include
from . import views
urlpatterns = [
  
     path('listings/',views.api_Listings),
     path('listing/<str:pk>/',views.individual_Listing)
]
