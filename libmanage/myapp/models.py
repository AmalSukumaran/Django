from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
    name = models.CharField(max_length = 255)
    age = models.BigIntegerField(null=True)
# creating the schema for the product table

class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.PositiveIntegerField()
    pic = models.ImageField(upload_to ="static/img/products/", null=True )#adding an image feild
    
