import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from wedding.models import Location, RSVP, Attendant
from wedding.utils.ip import get_client_ip


@login_required
def home(request):
    lang = request.GET.get('l', 'en')

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

    ip_address = get_client_ip(request)

    rsvp = RSVP.objects.filter(ip_address=ip_address).first()
    print(rsvp)

    return render_to_response("{0}.html".format(lang), {'existing_rsvp': rsvp,
                                                        'hotels_trani': hotels_trani,
                                                        'hotels_barletta': hotels_barletta,
                                                        'bandb_barletta': bandb_barletta,
                                                        'bandb_trani': bandb_trani},
                              context_instance=RequestContext(request))


@login_required
def guests(request):
    attendees = Attendant.objects.exclude(dietary_requirements='None').all()

    return render_to_response("guests_diet.html", {'attendees': attendees})


@login_required
@csrf_exempt
@require_http_methods(["POST"])
def accept_rsvp(request):
    ip_address = get_client_ip(request)

    family_name = request.POST.get('family_name', None)
    attending = request.POST.get('attending')
    address = request.POST.get('address', '')

    attendees = request.POST.get('guest_details', '[]')
    attendees = json.loads(attendees)

    attending = (attending == 'true')

    existing_rsvp = RSVP.objects.filter(ip_address=ip_address).count() != 0

    if existing_rsvp:
        return JsonResponse({'success': False, type: 'existing_rsvp',
                             'message': 'An existing RSVP is in our system from the same IP adrdress.'})
    else:
        rsvp = RSVP(ip_address=ip_address, family_name=family_name, attending=attending, address=address)
        rsvp.save()

        for attendee in attendees:
            type = attendee['adultchild']

            attendant = Attendant(first_name=attendee['firstname'], last_name=attendee['lastname'],
                                  nationality=attendee['nationality'],
                                  type=type,
                                  dietary_requirements=attendee['dietrequirements'])
            attendant.save()
            rsvp.attendees.add(attendant)

        return JsonResponse({'success': True})
