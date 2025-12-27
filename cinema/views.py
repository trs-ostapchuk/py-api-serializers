from rest_framework import viewsets

from cinema.models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
)
from cinema.serializers import (
    CinemaHallSerializer,
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving,
    updating and deleting cinema halls.
    """
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
