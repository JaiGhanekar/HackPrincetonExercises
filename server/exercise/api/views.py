from django.shortcuts import render
from rest_framework import viewsets
from models import *
from serializers import *
# Create your views here.

class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all().order_by('user_id')
    serializer_class =  AthleteSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class OrientationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Orientation.objects.all()
    serializer_class = OrientationSerializer


class ScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
