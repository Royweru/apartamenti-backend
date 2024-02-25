from django.urls import path,include
from . import views
urlpatterns = [
  
     path('listings/',views.getListings),
     path('listing/<str:pk>/',views.getListing)
]
