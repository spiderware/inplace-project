#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.measure import D

class Location(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='locations')
    location = models.PointField(null=True, blank=True)

    objects = models.GeoManager()

    class Meta:
        get_latest_by = 'modified_at'

    def __unicode__(self):
        return u"%s (%s)" % (self.user, self.location)

    def nearby(self, distance=None):
        """
from inplace_core.models import *
sf = Person.objects.get(id=2)
sf.nearby_people()
        """
        distance = distance or D(km=10)
        return Location.objects.filter(
                    location__distance_lt=(self.location, distance)
                    ).exclude(pk=self.pk)
