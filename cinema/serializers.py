from rest_framework import serializers

from cinema.models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
)


class CinemaHallSerializer(serializers.ModelSerializer):
    """
    Model serializer for the CinemaHall entity
    """
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class GenreSerializer(serializers.ModelSerializer):
    """
    Model serializer for the Genre entity
    """
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    """
    Model serializer for the Actor entity
    """
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class MovieSerializer(serializers.ModelSerializer):
    """
    Model serializer for the Movie entity
    """
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors"
        )
