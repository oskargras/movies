from .models import Movie, Person
from rest_framework import serializers


# Tworzę serialaizer dla Person
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


#Tworzę serialaizer dla Movie
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    director = serializers.HyperlinkedIdentityField(view_name="person-detail", read_only=True)
    actors = PersonSerializer(many=True)
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "director", "actors", "year")

