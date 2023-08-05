from django.urls import path
from rest_framework.routers import DefaultRouter
from measurement.views import SensorsViewSet, MeasurementsViewSet, SensorViewSet

r = DefaultRouter()
r.register(r"sensors", SensorViewSet) ## � ��������� SensorsViewSet ���������� ��������� �� �� ���� �������
r.register('measurements', MeasurementsViewSet)
r.register(r"sensors/<pk>/", SensorsViewSet)

urlpatterns = r.urls
