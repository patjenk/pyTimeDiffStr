from calendar import monthrange


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
        # Handle "X months and ..."
        num_months = (datetime_one.year - datetime_two.year) * 12 + (datetime_one.month - datetime_two.month)
        if datetime_one.day < datetime_two.day:
            num_weeks = (datetime_two.day - datetime_one.day) / 7
        else:
            num_weeks = ((monthrange(datetime_one.year, datetime_one.month)[1]-datetime_one.day) + datetime_two.day) / 7
        if num_weeks > 1:
            if datetime_one.day < datetime_two.day:
                num_months -= 1
            return "{} months and {:.0f} weeks ago".format(int(num_months), num_weeks)
        else:
            return "{} months ago".format(int(num_months))
    elif datetime_one.day == datetime_two.day and datetime_one.month == datetime_two.month and abs(datetime_one.year - datetime_two.year) <= 2:
        return "1 year ago"
    elif delta.days < 365 + (7 * 4):
        # Handle "1 year and X weeks"
        num_weeks = (delta.days - 365) / 7
        return "1 year and {:.0f} weeks ago".format(num_weeks)
    else:
        num_years = (datetime_one.year - datetime_two.year)
        if datetime_one.month < datetime_two.month:
            num_months = datetime_one.month
        else:
            num_months = datetime_one.month - datetime_two.month
        return "{} years and {} months ago".format(int(num_years), int(num_months))
