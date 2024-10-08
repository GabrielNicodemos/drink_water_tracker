# Generated by Django 5.1 on 2024-08-12 17:51

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
                ('daily_goal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DrinkWater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_drink_water', models.DateField(default=django.utils.timezone.now)),
                ('quantity_ml', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drink_water_tracker.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='DailyGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('goal_achieved', models.BooleanField(default=False)),
                ('total_consumption', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drink_water_tracker.userprofile')),
            ],
        ),
    ]
