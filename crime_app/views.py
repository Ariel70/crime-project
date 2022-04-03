from django.shortcuts import render
from rest_framework import viewsets
from crime_app.serializers import CrimeSerializer
from crime_app.models import Crime
from django.http import JsonResponse


# Create your views here.
class CrimeViewSet(viewsets.ModelViewSet):
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer


def predicted(request):
    data = {
        'Violence Against the Person': 339488,
        'Theft': 265069,
        'Vehicle Offences': 146776,
        'Public order Offences': 86324,
        'Burglary': 78732,
        'Arson and Criminal Damage': 76762,
        'Drug Offences': 66351,
        'Sexual Offences': 33812,
        'Robbery': 33394,
        'Miscellaneous Crimes Against Society': 16876,
        'Possession of Weapons': 8360,
        'Historical Fraud and Forgery': 1
    }
    return JsonResponse(data)
