from django.contrib import admin
from drink_water_tracker.models import UserProfile, DrinkWater, DailyGoal

class UserProfiles(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight', 'daily_goal')
    list_display_links = ('id', 'name')
    list_per_page = 20
    search_fields = ('name',)

admin.site.register(UserProfile, UserProfiles)

class DrinkWaters(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_drink_water', 'quantity_ml')
    list_display_links = ('id',)
    search_fields = ('user',)

admin.site.register(DrinkWater, DrinkWaters)

class DailyGoals(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'goal_achieved', 'total_consumption')
    list_display_links = ('id',)
    search_fields = ('user',)


admin.site.register(DailyGoal, DailyGoals)