from datetime import datetime
from unittest import TestCase

from pyTimeDiffStr.timediffstr import timediffstr


class TestTimeDiffStr(TestCase):

    def test_three_days(self):
        """
        Test dates two dates that are three days apart.
        """
        datetime_one = datetime(year=2020, month=1, day=4, hour=5, minute=1)
        datetime_two = datetime(year=2020, month=1, day=1, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "3 days ago")
