def timediffstr(datetime_one, datetime_two):
    """
    Return a str describing the difference between two dates (e.g. "1 year and 2 weeks ago")
    """
    delta = datetime_one - datetime_two

    if delta.days == 0:
        return "earlier today"
    elif delta.days == 1:
        return "yesterday"
    elif delta.days < 7:
        return "{} days ago".format(delta.days)
    elif delta.days == 7:
        return "{} week".format(int(delta.days/7))
    elif delta.days < 14:
        return "{} days ago".format(delta.days)
    elif delta.days < 60:
        return "{} weeks ago".format(int(delta.days/7))
    elif delta.days < 364:
        num_months = (datetime_one.year - datetime_two.year) * 12 + (datetime_one.month - datetime_two.month)
        return "{} months ago".format(int(num_months))
    elif datetime_one.day == datetime_two.day and datetime_one.month == datetime_two.month and (datetime_one.year - datetime_two.year) == 1:
        return "1 year ago"
    else:
        num_years = (datetime_one.year - datetime_two.year)
        if datetime_one.month < datetime_two.month:
            num_months = datetime_one.month
        else:
            num_months = datetime_one.month - datetime_two.month
        return "{} years and {} months ago".format(int(num_years), int(num_months))
