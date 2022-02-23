from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import *
from .models import *


class DailyActivityViewSet(viewsets.ModelViewSet):
    queryset = DailyActivity.objects.all()
    serializer_class = DailyActivitySerializer



class SleepDaySerializerViewSet(viewsets.ModelViewSet):
    queryset = SleepDay.objects.all()
    serializer_class = SleepDaySerializer
    
    

class HourlyCaloriesViewSet(viewsets.ModelViewSet):
    queryset = HourlyCalories.objects.all()
    serializer_class = HourlyCaloriesSerializer