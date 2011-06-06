#-*- coding: utf-8 -*-
from .models import Location
from django.contrib.auth.models import User
import random

def create(start=1, amount=100):
    for i in range(start, amount):
        user = User.objects.get_or_create(username="user%s" % i)[0]
        x = float(random.randint(-50000,50000))/1000.0
        y = float(random.randint(-50000,50000))/1000.0
        location = Location(user=user, location='POINT(%s %s)' % (x,y))
        location.save()