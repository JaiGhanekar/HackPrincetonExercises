from models import *
from rest_framework import serializers

class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Athlete
        fields = ('username','first_name', 'last_name', 'email', 'groups', 'goal', 'user')


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercise
        fields = ('performer', 'name')


class OrientationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orientation
        fields = ('exercise', 'x', 'y', 'z')

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ('point, maximum')




