from django.urls import path
from rest_framework.routers import DefaultRouter
from measurement.views import SensorsViewSet, MeasurementsViewSet, SensorViewSet

r = DefaultRouter()
r.register('sensor', SensorViewSet) 
r.register('measurements', MeasurementsViewSet)
r.register('sensors', SensorsViewSet)

urlpatterns = r.urls
