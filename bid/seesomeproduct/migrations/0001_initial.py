# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-31 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biddingprice',
            fields=[
                ('biddingid', models.AutoField(primary_key=True, serialize=False)),
                ('bidder', models.CharField(max_length=100)),
                ('Bid_on_productid', models.IntegerField(default=0)),
                ('biddingprice', models.IntegerField(default=0)),
            ],
        ),
    ]