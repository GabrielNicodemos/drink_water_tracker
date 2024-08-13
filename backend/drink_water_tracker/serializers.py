from rest_framework import serializers
from drink_water_tracker.models import UserProfile, DrinkWater, DailyGoal

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class DrinkWaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkWater
        fields = '__all__'

class DailyGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyGoal
        fields = '__all__'

class UserCompletedGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyGoal
        fields = '__all__'

class UserCompletedGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyGoal
        fields = '__all__'


class ListUserHistoryGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyGoal
        fields = '__all__'

class ListUserDailyGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyGoal
        fields = '__all__'
