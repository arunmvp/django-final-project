from django.db import models

# Create your models here.

class setcategory(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category 

class feature_products(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.URLField()
    price = models.IntegerField()
    category = models.ForeignKey(setcategory , on_delete=models.CASCADE)  
    
    def __str__(self):
        return self.title





