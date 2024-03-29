from datetime import datetime, timedelta
from unittest import TestCase

from pyTimeDiffStr.timediffstr import timediffstr


class TestTimeDiffStr(TestCase):

    def test_3_days(self):
        """
        Test dates two dates that are three days apart.
        """
        datetime_one = datetime(year=2020, month=1, day=4, hour=5, minute=1)
        datetime_two = datetime(year=2020, month=1, day=1, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "3 days ago")

    def test_2_months_2_weeks(self):
        """
        Test 4/7/2021 to 1/20/2021.
        """
        datetime_one = datetime(year=2021, month=4, day=7, hour=5, minute=1)
        datetime_two = datetime(year=2021, month=1, day=20, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "2 months, 2 weeks, and 4 days ago")

    def test_2_months_4_weeks(self):
        """
        Test 4/14/2021 to 1/20/2021.

        This one is weird. It's the third Wednesday in January to the second
        Wednesday in April. So its not three full months. But its four weeks
        after the third Wednesay in March. So we say it's 4 weeks.
        """
        datetime_one = datetime(year=2021, month=4, day=14, hour=5, minute=1)
        datetime_two = datetime(year=2021, month=1, day=20, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "2 months, 3 weeks, and 4 days ago")

    def test_3_months_2_weeks(self):
        """
        Test 4/17/2021 to 1/2/2021.
        """
        datetime_one = datetime(year=2021, month=4, day=17, hour=5, minute=1)
        datetime_two = datetime(year=2021, month=1, day=2, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "3 months, 2 weeks, and 1 day ago")

    def test_4_months_2_weeks(self):
        """
        Test 4/5/2021 to 11/16/2020.
        """
        datetime_one = datetime(year=2021, month=4, day=5, hour=5, minute=1)
        datetime_two = datetime(year=2020, month=11, day=16, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "4 months, 2 weeks, and 6 days ago")

    def test_4_months_2_weeks_2(self):
        """
        Test 4/5/2021 to 11/17/2020.
        """
        datetime_one = datetime(year=2021, month=4, day=5, hour=5, minute=1)
        datetime_two = datetime(year=2020, month=11, day=16, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "4 months, 2 weeks, and 6 days ago")

    def test_4_months_2_weeks_3(self):
        """
        Test 4/20/2021 to 12/1/2020.
        """
        datetime_one = datetime(year=2021, month=4, day=20, hour=5, minute=1)
        datetime_two = datetime(year=2020, month=12, day=1, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "4 months, 2 weeks, and 5 days ago")

    def test_4_months_2_weeks_4(self):
        """
        Test 5/4/2021 to 1/19/2021.
        """
        datetime_one = datetime(year=2021, month=4, day=20, hour=5, minute=1)
        datetime_two = datetime(year=2020, month=12, day=1, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "4 months, 2 weeks, and 5 days ago")


    def test_8_months(self):
        """
        Test 4/1/2021 to 8/6/2020.
        """
        datetime_one = datetime(year=2021, month=4, day=1, hour=5, minute=1)
        datetime_two = datetime(year=2020, month=8, day=6, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "7 months, 3 weeks, and 5 days ago")

    def test_1_year(self):
        """
        Test dates two dates that are one year apart.
        """
        datetime_one = datetime(year=2021, month=1, day=1, hour=5, minute=1)
        datetime_two = datetime(year=2020, month=1, day=1, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "1 year ago")

    def test_1_year_2_weeks(self):
        """
        Test 4/1/2021 to 8/6/2020.
        """
        datetime_one = datetime(year=2021, month=4, day=3, hour=5, minute=1)
        datetime_two = datetime(year=2020, month=3, day=21, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "1 year, 1 week, and 6 days ago")

    def test_1_year_2_weeks_2(self):
        """
        Test 4/14/2021 to 4/1/2020.
        """
        datetime_one = datetime(year=2021, month=4, day=14, hour=5, minute=1)
        datetime_two = datetime(year=2020, month=4, day=1, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "1 year, 1 week, and 6 days ago")

    def test_11_months_1_week(self):
        """
        Test 10/9/2021 to 10/31/2020.
        """
        datetime_one = datetime(year=2021, month=10, day=9, hour=5, minute=1)
        datetime_two = datetime(year=2020, month=10, day=31, hour=5, minute=1)
        self.assertEqual(timediffstr(datetime_one, datetime_two), "11 months, 1 week, and 2 days ago")

    def test_10_year_stress(self):
        """
        make sure we return a str
        """
        datetime_one = datetime(year=2021, month=1, day=1, hour=5, minute=1)
        datetime_two = datetime_one - timedelta(days=1)
        for days in range (0, 365*10):
            result = timediffstr(datetime_one, datetime_two)
            self.assertTrue(isinstance(result, str))
            self.assertTrue(len(result) > 5)
            datetime_two = datetime_two - timedelta(days=1)

    def test_1month_xdays(self):
        """
        """
        datetime_one = datetime(year=2021, month=1, day=1, hour=5, minute=1)
        datetime_two = datetime_one + timedelta(days=92)
        for days in range (2, 6):
            result = timediffstr(datetime_two, datetime_one)
            self.assertTrue(isinstance(result, str))
            self.assertEqual(result, "3 months and {} days ago".format(days))
            datetime_two = datetime_two + timedelta(days=1)
