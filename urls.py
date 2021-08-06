from django.urls import path
from .views import CovidView

urlpatterns = [
    path('', CovidView, name='covid'),
]
