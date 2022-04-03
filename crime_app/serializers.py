from rest_framework import serializers

from crime_app.models import Crime


class CrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crime
        fields = ('date', 'borough', 'description', 'count')
