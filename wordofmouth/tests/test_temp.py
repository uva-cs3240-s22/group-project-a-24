from django.test import TestCase
from wordofmouth.models import Temp
import datetime
from django.utils import timezone
# Create your tests here.


class TempModelTests(TestCase):

    def test_temp_was_published_recently(self):
        """
        :return: true if a Temp model was created within the past day
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_temp = Temp(temp_date=time)
        self.assertIs(recent_temp.was_published_recently(), True)
