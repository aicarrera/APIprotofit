
# serializers.py
from rest_framework import serializers

from .models import *

class HourlyCaloriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HourlyCalories
        fields = ('user_id', 'activityhour', 'calories')

        
        
class SleepDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepDay
        fields = ('user_id', 'sleepday', 'totalsleeprecords')


class DailyActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyActivity
        fields = ('user_id', 'activitydate', 'totalsteps','totaldistance')
