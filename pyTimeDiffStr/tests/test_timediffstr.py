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

    def test_one_year(self):
        """
        Test dates two dates that are one year apart.
        """
        datetime_one = datetime(year=2021, month=1, day=1, hour=5, minute=1)
        datetime_two = datetime(year=2020, month=1, day=1, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "1 year ago")

    def test_8_months(self):
        """
        Test 4/1/2021 to 8/6/2020.
        """
        datetime_one = datetime(year=2021, month=4, day=1, hour=5, minute=1)
        datetime_two = datetime(year=2020, month=8, day=6, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "8 months ago")

    def test_1_year_2_weeks(self):
        """
        Test 4/1/2021 to 8/6/2020.
        """
        datetime_one = datetime(year=2021, month=4, day=3, hour=5, minute=1)
        datetime_two = datetime(year=2020, month=3, day=21, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "1 year and 2 weeks ago")

    def test_1_year_2_weeks(self):
        """
        Test 4/5/2021 to 11/16/2020.
        """
        datetime_one = datetime(year=2021, month=4, day=5, hour=5, minute=1)
        datetime_two = datetime(year=2020, month=11, day=16, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "4 months and 2 weeks ago")
