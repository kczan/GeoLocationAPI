from django.db import models


class GeoLocationData(models.Model):
    ip = models.CharField(max_length=15, unique=True)
    type = models.CharField(max_length=10)
    continent_code = models.CharField(max_length=2)
    continent_name = models.CharField(max_length=15)
    country_code = models.CharField(max_length=5)
    country_name = models.CharField(max_length=50)
    region_code = models.CharField(max_length=5)
    region_name = models.CharField(max_length=40)
    city = models.CharField(max_length=80)
    zip = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()
