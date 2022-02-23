# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DailyActivity(models.Model):
    user_id = models.BigIntegerField()
    activitydate = models.DateField()
    totalsteps = models.DecimalField(max_digits=20, decimal_places=15)
    totaldistance = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    trackerdistance = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    loggedactivitiesdistance = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    veryactivedistance = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    moderatelyactivedistance = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    lightactivedistance = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    sedentaryactivedistance = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    veryactiveminutes = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    fairlyactiveminutes = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    lightlyactiveminutes = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    sedentaryminutes = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    calories = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'daily_activity'
        unique_together = (('user_id', 'activitydate'),)


class HourlyCalories(models.Model):
    user_id = models.BigIntegerField()
    activityhour = models.DateTimeField()
    calories = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'hourly_calories'
        unique_together = (('user_id', 'activityhour'),)


class SleepDay(models.Model):
    user_id = models.BigIntegerField()
    sleepday = models.DateField()
    totalsleeprecords = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    totalminutesasleep = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    totaltimeinbed = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'sleep_day'

