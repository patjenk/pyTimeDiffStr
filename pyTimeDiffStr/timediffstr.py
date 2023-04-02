from calendar import monthrange
from decimal import Decimal
import math


def timediffstr(datetime_one, datetime_two):
    """
    Return a str describing the difference between two dates (e.g. "1 year and 2 weeks ago")
    """
    if datetime_two > datetime_one:
        daettime_one, datetime_two = datetime_two, datetime_one

    delta = datetime_one - datetime_two

    if delta.days == 0:
        return "earlier today"
    elif delta.days == 1:
        return "yesterday"
    elif delta.days < 7:
        return "{} days ago".format(delta.days)
    elif delta.days == 7:
        return "1 week"
    elif delta.days < 14:
        return "{} days ago".format(delta.days)
    elif delta.days < 60:
        return "{} weeks ago".format(delta.days//7)
    elif delta.days < 365:
        months = (delta.days % 365) // 30
        weeks = ((delta.days % 365) % 30) // 7
        days = ((delta.days % 365) % 30) % 7
        if months > 1 and weeks == 0 and days == 0:
            return "{} months ago".format(months)
        elif months > 1 and weeks == 0 and days == 1:
            return "{} months and 1 day ago".format(months)
        elif months > 1 and weeks == 0 and days > 0:
            return "{} months and {} days ago".format(months, days)
        elif months > 1 and weeks == 1 and days == 0:
            return "{} months and 1 week ago".format(months)
        elif months > 1 and weeks == 1 and days == 1:
            return "{} months, 1 week, and 1 day ago".format(months)
        elif months > 1 and weeks == 1 and days > 0:
            return "{} months, 1 week, and {} days ago".format(months, days)
        elif months > 1 and weeks > 1 and days == 0:
            return "{} months and {} weeks ago".format(months, weeks)
        elif months > 1 and weeks > 1 and days == 1:
            return "{} months, {} weeks, and 1 day ago".format(months, weeks)
        elif months > 1 and weeks > 1 and days > 0:
            return "{} months, {} weeks, and {} days ago".format(months, weeks, days)
    else:
        years = delta.days // 365
        months = (delta.days % 365) // 30
        weeks = ((delta.days % 365) % 30) // 7
        days = ((delta.days % 365) % 30) % 7
        if years == 1:
            if months == 0 and weeks == 0 and days == 0:
                return "1 year ago"
            elif months == 0 and weeks == 0 and days == 1:
                return "1 year and 1 day ago"
            elif months == 0 and weeks == 0 and days > 0:
                return "1 year and {} days ago".format(days)
            elif months == 0 and weeks == 1 and days == 0:
                return "1 year and 1 week ago"
            elif months == 0 and weeks == 1 and days == 1:
                return "1 year, 1 week, and 1 day ago"
            elif months == 0 and weeks == 1 and days > 0:
                return "1 year, 1 week, and {} days ago".format(days)
            elif months == 0 and weeks > 1 and days == 0:
                return "1 year, {} weeks, and {} days ago".format(weeks, days)
            elif months == 1 and weeks == 0 and days == 0:
                return "1 year and 1 month ago"
            elif months == 1 and weeks == 0 and days == 1:
                return "1 year, 1 month, and 1 day ago"
            elif months == 1 and weeks == 0 and days > 0:
                return "1 year, 1 month, and {} days ago".format(days)
            elif months == 1 and weeks == 1 and days == 0:
                return "1 year, 1 month, and 1 week ago"
            elif months == 1 and weeks == 1 and days == 1:
                return "1 year, 1 month, 1 week, and 1 day ago"
            elif months == 1 and weeks > 1 and days > 0:
                return "1 year, 1 month, {} weeks, and {} days ago".format(weeks, days)
            elif months > 1 and weeks == 0 and days == 0:
                return "1 year and {} months ago".format(months)
            elif months > 1 and weeks == 0 and days == 1:
                return "1 year, {} months, and 1 day ago".format(months)
            elif months > 1 and weeks == 0 and days > 0:
                return "1 year, {} months, and {} days ago".format(months, days)
            elif months > 1 and weeks == 1 and days == 0:
                return "1 year, {} months, and 1 week ago".format(months)
            elif months > 1 and weeks == 1 and days == 1:
                return "1 year, {} months, 1 week, and 1 day ago".format(months)
            elif months > 1 and weeks == 1 and days > 0:
                return "1 year, {} months, 1 week, and {} days ago".format(months, days)
            elif months > 1 and weeks > 1 and days > 0:
                return "1 year, {} months, {} weeks, and {} days ago".format(months, weeks, days)
        else:
            if months == 0 and weeks == 0 and days == 0:
                return "{} years ago".format(years)
            elif months == 0 and weeks == 0 and days == 1:
                return "{} years and 1 day ago".format(years)
            elif months == 0 and weeks == 0 and days > 0:
                return "{} years and {} days ago".format(years, days)
            elif months == 0 and weeks == 1 and days == 0:
                return "{} years and 1 week ago".format(years)
            elif months == 0 and weeks == 1 and days == 1:
                return "{} years, 1 week, and 1 day ago".format(years)
            elif months == 0 and weeks == 1 and days > 0:
                return "{} years, 1 week, and {} days ago".format(years, days)
            elif months == 0 and weeks > 1 and days == 1:
                return "{} years, {} weeks, and 1 day ago".format(years, weeks)
            elif months == 0 and weeks > 1 and days > 0:
                return "{} years, {} weeks, and {} days ago".format(years, weeks, days)
            elif months == 1 and weeks == 0 and days == 0:
                return "{} years and 1 month ago".format(years)
            elif months == 1 and weeks == 0 and days == 1:
                return "{} years, 1 month, and day ago".format(years)
            elif months == 1 and weeks == 0 and days > 0:
                return "{} years, 1 month, and {} days ago".format(years, days)
            elif months == 1 and weeks == 1 and days == 0:
                return "{} years, 1 month, and 1 week ago".format(years)
            elif months == 1 and weeks == 1 and days == 1:
                return "{} years, 1 month, 1 week, and 1 day ago".format(years)
            elif months == 1 and weeks == 1 and days > 0:
                return "{} years, 1 month, 1 week, and {} days ago".format(years, days)
            elif months == 1 and weeks > 1 and days == 1:
                return "{} years, 1 month, {} weeks, and 1 day ago".format(years, weeks)
            elif months == 1 and weeks > 1 and days > 0:
                return "{} years, 1 month, {} weeks, and {} days ago".format(years, weeks, days)
            elif months > 1 and weeks == 0 and days == 0:
                return "{} years and {} months ago".format(years, months)
            elif months > 1 and weeks == 0 and days == 1:
                return "{} years, {} months, and 1 day ago".format(years, months)
            elif months > 1 and weeks == 0 and days > 0:
                return "{} years, {} months, and {} days ago".format(years, months, days)
            elif months > 1 and weeks == 1 and days == 0:
                return "{} years, {} months, and 1 week ago".format(years, months)
            elif months > 1 and weeks == 1 and days == 1:
                return "{} years, {} months, 1 week, and 1 day ago".format(years, months)
            elif months > 1 and weeks == 1 and days > 0:
                return "{} years, {} months, 1 week, and {} days ago".format(years, months, days)
            elif months > 1 and weeks > 1 and days == 0:
                return "{} years, {} months, and {} weeks ago".format(years, months, weeks)
            elif months > 1 and weeks > 1 and days == 1:
                return "{} years, {} months, {} weeks, and 1 day ago".format(years, months, weeks)
            elif months > 1 and weeks > 1 and days > 0:
                return "{} years, {} months, {} weeks, and {} days ago".format(years, months, weeks, days)

