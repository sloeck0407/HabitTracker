from datetime import datetime
from turtle import done


def make_habit(habit_name, regularity, start_date, current_date, status):
   
    # time elapsed since you broke the habit in seconds
    time_elapsed = (datetime.now() - start_date).total_seconds()  # the start date should be automatically saved, from the first time the user checks that habit

    # convert timestamp into hours/days
    hours = round(time_elapsed / 3600, 2)
    days = round(hours / 24, 2)

    # streak, for getting a certain streak, you will get some words of encouragement
    streak = round(days)

    # convert hours to days, have months (30 and 31 days) and years
    if hours > 72:
        hours = str(days) + 'days'
    else:
        hours = str(hours) + 'hours'

    # status only either done or not done
    if status == "done":
        status = "You did it" # or some other kind of checkmark
    if status == "not done":
        status ="You're almost there!"


    return {'habit': habit_name, 'regularity': regularity, 'start_date': start_date, 'streak': hours, 'status': status}

print(make_habit("workout", "daily", datetime(2023, 1, 1, 12, 00), datetime.now(), status="not done"))