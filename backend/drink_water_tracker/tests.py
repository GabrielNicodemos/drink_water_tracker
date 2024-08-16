from django.test import TestCase
from .models import UserProfile, DrinkWater
from django.utils import timezone
import pytz


class UserProfileModelTests(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create(name="Gabriel", weight=90)

    def test_user_profile_creation(self):
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(self.user.name, "Gabriel")
        self.assertEqual(self.user.weight, 90)

    def test_user_profile_update(self):
        self.user.name = "Eduardo"
        self.user.save()
        updated_user = UserProfile.objects.get(id=self.user.id)
        self.assertEqual(updated_user.name, "Eduardo")

    def test_user_profile_deletion(self):
        self.user.delete()
        self.assertEqual(UserProfile.objects.count(), 0)

class DrinkWaterModelTests(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create(name="Gabriel", weight=90)
        saopaulo_tz = pytz.timezone('America/Sao_Paulo')
        today = timezone.now().astimezone(saopaulo_tz).date()
        self.drink_water = DrinkWater.objects.create(
            user=self.user,
            date_drink_water=today,
            quantity_ml=1000
        )

    def test_drink_water_creation(self):
        self.assertEqual(DrinkWater.objects.count(), 1)
        self.assertEqual(self.drink_water.quantity_ml, 1000)
        self.assertEqual(self.drink_water.user, self.user)

    def test_drink_water_update(self):
        self.drink_water.quantity_ml = 1500
        self.drink_water.save()
        updated_drink_water = DrinkWater.objects.get(id=self.drink_water.id)
        self.assertEqual(updated_drink_water.quantity_ml, 1500)

    def test_drink_water_deletion(self):
        self.drink_water.delete()
        self.assertEqual(DrinkWater.objects.count(), 0)
