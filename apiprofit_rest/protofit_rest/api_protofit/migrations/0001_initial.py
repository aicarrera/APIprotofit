# Generated by Django 4.0.2 on 2022-02-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('activitydate', models.DateField()),
                ('totalsteps', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('totaldistance', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('trackerdistance', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('loggedactivitiesdistance', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('veryactivedistance', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('moderatelyactivedistance', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('lightactivedistance', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('sedentaryactivedistance', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('veryactiveminutes', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('fairlyactiveminutes', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('lightlyactiveminutes', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('sedentaryminutes', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('calories', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'daily_activity',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HourlyCalories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('activityhour', models.DateTimeField()),
                ('calories', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'hourly_calories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SleepDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('sleepday', models.DateField()),
                ('totalsleeprecords', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('totalminutesasleep', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('totaltimeinbed', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'sleep_day',
                'managed': False,
            },
        ),
    ]