from rest_framework import serializers
from .models import Shelter, PendingCheckin

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = '__all__'

class PendingCheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingCheckin
        fields = '__all__'