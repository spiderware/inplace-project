#-*- coding: utf-8 -*-
from django.contrib.gis import admin
from .models import Location

class LocationAdmin(admin.OSMGeoAdmin):
    list_display = ('user', 'location')

admin.site.register(Location, LocationAdmin)
