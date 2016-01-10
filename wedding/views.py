from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext

from wedding.models import Location


@login_required
def home(request):
    hotels_trani = Location.objects.filter(town='Trani',
                                          type='H').order_by(
            'distance_km_from_cathedral')


    hotels_barletta = Location.objects.filter(town='Barletta',
                                             type='H').order_by(
            'distance_km_from_cathedral')
    bandb_trani = Location.objects.filter(town='Trani',
                                         type='B').order_by(
            'distance_km_from_cathedral')
    bandb_barletta = Location.objects.filter(town='Barletta', type='B').order_by('distance_km_from_cathedral')

    return render_to_response("main.html", {'hotels_trani': hotels_trani,
                                            'hotels_barletta': hotels_barletta,
                                            'bandb_barletta': bandb_barletta,
                                            'bandb_trani': bandb_trani},
                              context_instance=RequestContext(request))
