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
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieListSerializer,
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving,
    updating and deleting cinema halls.
    """
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving,
    updating and deleting genres.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving,
    updating and deleting actors.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving,
    updating and deleting actors.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return MovieSerializer
