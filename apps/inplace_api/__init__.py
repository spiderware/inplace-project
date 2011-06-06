#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django_xmlrpc.decorators import xmlrpc_func, permission_required
from inplace_core.models import Location

@permission_required(perm='can_use_api')
@xmlrpc_func(returns='list', args=[])
def get_nearby_people(username):
    location = Location.objects.filter(user__username=username).latest()
    nearby = []
#    print username, location
    for location in location.nearby().select_related('user'):
        nearby.append({
            'username': location.user.username,
            'latitude': location.location[0],
            'longitude': location.location[1],
        })
    return nearby


@permission_required(perm='can_use_api')
@xmlrpc_func(returns='boolean', args=['float', 'float'])
def set_my_location(username, latitude, longitude):
    """
    like set location but only for the logged in user.
    """
#    print username, latitude, longitude
    user = User.objects.get_or_create(username=username)[0]
    location = Location.objects.get_or_create(user=user)[0]
    location.location = 'POINT(%s %s)' % (latitude,longitude)
    location.save()
    return True