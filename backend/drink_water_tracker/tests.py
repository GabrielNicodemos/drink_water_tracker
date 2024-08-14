from django.test import TestCase

from .models import UserProfile, DrinkWater
from django.utils import timezone
import pytz


class DrinkWaterModelTests(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create(name="Gabriel", weight=90)

        saopaulo_tz = pytz.timezone('America/Sao_Paulo')
        today = timezone.now().astimezone(saopaulo_tz).date()
        DrinkWater.objects.create(
            user=self.user,
            date_drink_water=today,
            quantity_ml=1000
        )
