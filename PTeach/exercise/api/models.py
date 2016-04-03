# Create your models here.
from django.db import models
from django.contrib.auth.models import User 
class Athlete(models.Model):
    """Fields from default User model:
    username
    first_name
    last_name
    email #require a school email
    password
    groups
    user_permissions
    is_staff
    is_active
    is_superuser
    last_login
    date_joined
    For more information, go to:
    https://docs.djangoproject.com/en/1.8/ref/contrib/auth/
    """

    goal = models.CharField(max_length=200, blank=False)
    user = models.OneToOneField(User)

class Exercise(models.Model):
    athlete = models.ForeignKey(Athlete, related_name='exercises')
    status = models.BooleanField()
    completed = models.BooleanField()
    name = models.CharField(max_length=200, blank=False)

class Orientation(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='orientations')
    x = models.DecimalField(max_digits = 6, decimal_places = 3)
    y = models.DecimalField(max_digits = 6, decimal_places = 3)
    z = models.DecimalField(max_digits = 6, decimal_places = 3)
    w = models.DecimalField(max_digits = 6, decimal_places = 3) 
    
class Score(models.Model):
    points = models.ForeignKey(Exercise, related_name='scores')
    maximum = models.IntegerField()


