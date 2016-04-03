from django.shortcuts import render
from rest_framework import viewsets
from models import *
from django.contrib.auth.models import User, Group
from serializers import *
# Create your views here.

class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all().order_by('-id')
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



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    
