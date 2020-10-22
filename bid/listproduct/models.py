# -*- coding: utf-8 -*-
from django.db import models

class listedproducts(models.Model):
    productid = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=100)
    productdesc = models.CharField(max_length=3000)
    productcategory = models.CharField(max_length=100)
    holdingtimeperiod = models.DateField()
    biddingtimeperiod = models.DateField()
    productprice = models.IntegerField(default=0)
    productImage = models.ImageField(upload_to='')

    def __str__(self):
        return self.productname