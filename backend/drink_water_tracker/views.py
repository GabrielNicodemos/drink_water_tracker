from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from django.utils import timezone
import pytz


from drink_water_tracker.models import UserProfile, DrinkWater, DailyGoal
from drink_water_tracker.serializers import (
    UserProfileSerializer,
    DrinkWaterSerializer,
    DailyGoalSerializer,
    UserCompletedGoalsSerializer,
    ListUserHistoryGoalSerializer,
    ListUserDailyGoalSerializer
)

class UserProfileViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name', 'weight']
    ordering_fields = ['name']
    serializer_class = UserProfileSerializer

class DrinkWaterViewset(viewsets.ModelViewSet):
    queryset = DrinkWater.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['user', 'date_drink_water']
    ordering_fields = ['date_drink_water']
    serializer_class = DrinkWaterSerializer

class DailyGoalViewset(viewsets.ModelViewSet):
    queryset = DailyGoal.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['date', 'user']
    ordering_fields = ['date']
    serializer_class = DailyGoalSerializer

class UserCompletedGoalsViewSet(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        all_goals_of_user = DailyGoal.objects.filter(user_id=user_id)
        completed_goals = all_goals_of_user.filter(goal_achieved=True)

        total_goals = all_goals_of_user.count()
        completed_goals_count = completed_goals.count()
        percentage_completed = (completed_goals_count / total_goals * 100) if total_goals > 0 else 0

        serializer = UserCompletedGoalsSerializer(completed_goals, many=True)

        return Response({
            "percentage_completed": percentage_completed,
            "completed_goals": serializer.data
        })

class ListUserHistoryGoalViewSet(generics.ListAPIView):
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return DailyGoal.objects.filter(user=user_id).order_by('-date')

    serializer_class = ListUserDailyGoalSerializer

class ListUserTodayGoalViewSet(generics.ListAPIView):
    def get_queryset(self):
        user_id = self.kwargs['user_id']

        saopaulo_tz = pytz.timezone('America/Sao_Paulo')
        today = timezone.now().astimezone(saopaulo_tz).date()

        return DailyGoal.objects.filter(user_id=user_id, date=today)

    serializer_class = ListUserDailyGoalSerializer
