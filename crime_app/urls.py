from django.urls import include, path

from rest_framework import routers

from crime_app.views import CrimeViewSet, predicted


router = routers.DefaultRouter()
router.register(r'crimes', CrimeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('predicted', predicted)
]
