from django.db import models



# Create your models here.

class Artist(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=40)
    qualification=models.CharField(max_length=20)
    category=models.CharField(max_length=100)
    about=models.CharField(max_length=10)

    class Meta:
        db_table="artist_signup"

class Product(models.Model):
    product_name=models.CharField(max_length=20)
    desc=models.CharField(max_length=100)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.ImageField(upload_to='product/')

    class Meta:
        db_table="add_product"