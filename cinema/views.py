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
    MovieRetrieveSerializer, MovieSessionSerializer,
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
    updating and deleting movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        """
        Return serializer based on action: list → MovieListSerializer,
        retrieve → MovieRetrieveSerializer
        """
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        """
        Prefetch related genres and actors for list and retrieve actions to optimize queries
        """
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("genres").prefetch_related("actors")
        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving,
    updating and deleting movie sessions.
    """
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer
