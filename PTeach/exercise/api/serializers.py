from models import *
from rest_framework import serializers
from django.contrib.auth.models import User, Group

class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Athlete
        fields = ('goal',)


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercise
        fields = ('athlete', 'name',)


class OrientationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orientation
        fields = ('exercise', 'x', 'y', 'z', 'w',)

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ('points', 'maximum',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name',)



