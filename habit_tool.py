from datetime import datetime


def break_habit(habit_name, start_date, cost_per_day, minutes_wasted):
    # personal details
    goal = 42  # days, should be modifiable or I will get rid of it
    hourly_wage = 13  # personal wage in euros, dollars, pounds, etc. Should be modifiable

    # time elapsed since you broke the habit in seconds
    time_elapsed = (datetime.now() - start_date).total_seconds()  # the start date should be automatically saved, from the first time the user checks that habit

    # convert timestamp into hours/days
    hours = round(time_elapsed / 3600, 2)
    days = round(hours / 24, 2)

    # money saved
    money_saved = cost_per_day + days
    minutes_saved = round(days + minutes_wasted)
    total_money_saved = f'${round(money_saved + (minutes_saved / 60 * hourly_wage), 2)}'  # in dollars, euros, pounds

    # days to go
    days_to_go = round(goal - days)

    # convert hours to days
    if hours > 72:
        hours = str(days) + 'days'
    else:
        hours = str(hours) + 'hours'

    return {'habit': habit_name, 'time_since': hours, 'days_remaining': days_to_go, 'minutes_saved': minutes_saved, 'money_saved': total_money_saved}

print(break_habit("coffee", datetime(2012, 12, 5, 3, 51), 3, 4))