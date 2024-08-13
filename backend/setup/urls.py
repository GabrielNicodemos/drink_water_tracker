
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from drink_water_tracker.views import (
    UserProfileViewset,
    DrinkWaterViewset,
    DailyGoalViewset,
    UserCompletedGoalsViewSet,
    ListUserHistoryGoalViewSet,
    ListUserTodayGoalViewSet
)

router = routers.DefaultRouter()
router.register('users', UserProfileViewset, basename="users")
router.register('drink_waters', DrinkWaterViewset, basename="drink_waters")
router.register('daily_goals', DailyGoalViewset, basename="daily_goals")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('users/<int:user_id>/completed-goals/', UserCompletedGoalsViewSet.as_view(), name='user-completed-goals'),
    path('daily_goals/<int:user_id>/history', ListUserHistoryGoalViewSet.as_view(), name='daily_goals-user-history'),
    path('daily_goals/<int:user_id>/today', ListUserTodayGoalViewSet.as_view(), name='daily_goals-user-today'),
]
