from rest_framework import viewsets
from .models import Shelter, PendingCheckin
from .serializers import ShelterSerializer, PendingCheckinSerializer

class ShelterViewSet(viewsets.ModelViewSet):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

class PendingCheckinViewSet(viewsets.ModelViewSet):
    queryset = PendingCheckin.objects.all()
    serializer_class = PendingCheckinSerializer