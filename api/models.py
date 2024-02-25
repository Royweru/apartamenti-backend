from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length= 200)
    
    def __str__(self):
        return self.name
    
   
class Listing(models.Model):
    title = models.CharField(max_length=1000)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    bathroomCount= models.IntegerField()
    price = models.FloatField()
    
    def __str__(self):
        return self.title
    
class Image(models.Model):
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE)
    url= models.URLField(max_length=200)
    