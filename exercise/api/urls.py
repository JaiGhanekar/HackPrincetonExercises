from django.conf.urls import url, include
from views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'^athletes', AthleteViewSet)
router.register(r'^exercises', ExerciseViewSet)
router.register(r'^orientations', OrientationViewSet)
router.register(r'^scores', ScoreViewSet)




urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]