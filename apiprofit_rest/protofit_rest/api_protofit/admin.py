from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(DailyActivity)
admin.site.register(SleepDay)
admin.site.register(HourlyCalories)

