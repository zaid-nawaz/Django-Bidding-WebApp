# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Biddingprice(models.Model):
    biddingid = models.AutoField(primary_key=True)
    bidder = models.CharField(max_length=100)
    Bid_on_productid = models.CharField(max_length=10)
    biddingprice = models.IntegerField(default=0)

    def __str__(self):
        return  self.bidder+ ' ' + 'productid_is' + self.Bid_on_productid