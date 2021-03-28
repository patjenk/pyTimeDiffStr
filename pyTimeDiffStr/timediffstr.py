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
    elif delta.days < 500:
        num_months = (today.year - self.date.year) * 12 + (today.month - self.date.month)
        return "{} months ago".format(int(num_months))
    else:
        num_years = (today.year - self.date.year)
        if today.month < self.date.month:
            num_months = self.date.month
        else:
            num_months = today.month - self.date.month
        return "{} years and {} months ago".format(int(num_years), int(num_months))
