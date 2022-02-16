from django.urls import path
from .views import MeasurementView,SensorViewUpdate,SensorsView
urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorViewUpdate.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
