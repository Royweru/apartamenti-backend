from django.contrib import admin
from .models import Category,Listing,Image

# Register your models here.

admin.site.register(Category)

admin.site.register(Listing)

admin.site.register(Image)