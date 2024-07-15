def time_convert(value, from_unit, to_unit):
    if value == '':
        return '-'

    hours_in_day = 24
    days_in_week = 7
    days_in_month = 30
    days_in_year = 365

    total_hours = 0
    if from_unit == 'Hours':
        total_hours = value
    elif from_unit == 'Days':
        total_hours = value * hours_in_day
    elif from_unit == 'Weeks':
        total_hours = value * hours_in_day * days_in_week
    elif from_unit == 'Months':
        total_hours = value * hours_in_day * days_in_month
    elif from_unit == 'Years':
        total_hours = value * hours_in_day * days_in_year
    else:
        return '-'

    result = ''

    if to_unit == 'Years':
        years = total_hours // (hours_in_day * days_in_year)
        remaining_days_after_years = (total_hours % (hours_in_day * days_in_year)) // hours_in_day
        months_in_years = remaining_days_after_years // days_in_month
        remaining_days_after_months_in_years = remaining_days_after_years % days_in_month
        result = f'{years} year{"s" if years != 1 else ""}, {months_in_years} month{"s" if months_in_years != 1 else ""}, and {remaining_days_after_months_in_years} day{"s" if remaining_days_after_months_in_years != 1 else ""}'
    elif to_unit == 'Months':
        months = total_hours // (hours_in_day * days_in_month)
        remaining_days_after_months = (total_hours % (hours_in_day * days_in_month)) // hours_in_day
        weeks_in_months = remaining_days_after_months // days_in_week
        remaining_days_after_weeks_in_months = remaining_days_after_months % days_in_week
        result = f'{months} month{"s" if months != 1 else ""}, {weeks_in_months} week{"s" if weeks_in_months != 1 else ""}, and {remaining_days_after_weeks_in_months} day{"s" if remaining_days_after_weeks_in_months != 1 else ""}'
    elif to_unit == 'Weeks':
        weeks = total_hours // (hours_in_day * days_in_week)
        remaining_days_after_weeks = (total_hours % (hours_in_day * days_in_week)) // hours_in_day
        result = f'{weeks} week{"s" if weeks != 1 else ""} and {remaining_days_after_weeks} day{"s" if remaining_days_after_weeks != 1 else ""}'
    elif to_unit == 'Days':
        days = total_hours // hours_in_day
        hours_in_days = total_hours % hours_in_day
        result = f'{days} day{"s" if days != 1 else ""} and {hours_in_days} hour{"s" if hours_in_days != 1 else ""}'
    else:
        result = f'{total_hours} hour{"s" if total_hours != 1 else ""}'

    print(result)