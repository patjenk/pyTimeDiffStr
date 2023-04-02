from datetime import datetime
from dateutil.relativedelta import relativedelta

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
    else:
        rel_delta = relativedelta(datetime_one, datetime_two)
        result_parts = []
        result = ""

        if rel_delta.years > 0:
            result_parts.append(f"{rel_delta.years} {'year' if rel_delta.years == 1 else 'years'}")
        if rel_delta.months > 0:
            result_parts.append(f"{rel_delta.months} {'month' if rel_delta.months == 1 else 'months'}")
        if rel_delta.weeks > 0:
            result_parts.append(f"{rel_delta.weeks} {'week' if rel_delta.weeks == 1 else 'weeks'}")

        days_diff = rel_delta.days - (rel_delta.weeks * 7)
        if days_diff > 0:
            result_parts.append(f"{days_diff} {'day' if days_diff == 1 else 'days'}")

        if len(result_parts) == 0:
            result = ''
        elif len(result_parts)== 1:
            result = result_parts[0]
        elif len(result_parts) == 2:
            result = ' and '.join(result_parts)
        else:
            result = ', '.join(result_parts[:-1]) + ', and ' + result_parts[-1]

        # add "ago" to the end of the string
        result += " ago"
        return result 
