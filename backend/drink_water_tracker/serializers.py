from rest_framework import serializers
from drink_water_tracker.models import UserProfile, DrinkWater, DailyGoal
from drink_water_tracker.validators import validate_positive_value, name_not_alpha
from django.core.validators import MinValueValidator

class UserProfileSerializer(serializers.ModelSerializer):
    weight = serializers.FloatField(validators=[MinValueValidator(0.0)])
    class Meta:
        model = UserProfile
        fields = '__all__'

        def validate(self, values):
            if name_not_alpha(values['name']):
                raise serializers.ValidationError({'name': 'The name must contain only letters'})

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

class ListUserHistoryGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyGoal
        fields = '__all__'

class ListUserDailyGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyGoal
        fields = '__all__'
