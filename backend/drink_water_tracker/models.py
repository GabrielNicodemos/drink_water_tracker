from django.db import models
from django.utils import timezone

class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    weight = models.FloatField(blank=False)
    daily_goal = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.daily_goal = int(self.weight * 35)
        super().save(*args, **kwargs)

class DrinkWater(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date_drink_water = models.DateField(default=timezone.now)
    quantity_ml = models.IntegerField(blank=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        daily_goal, created = DailyGoal.objects.get_or_create(
            user=self.user,
            date=self.date_drink_water
        )

        daily_goal.update_total_consumption(self.quantity_ml)


class DailyGoal(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    goal_achieved = models.BooleanField(default=False)
    total_consumption = models.IntegerField(default=0)

    def update_total_consumption(self, quantity):
        self.total_consumption += quantity
        self.goal_achieved = self.total_consumption >= self.user.daily_goal
        self.save()