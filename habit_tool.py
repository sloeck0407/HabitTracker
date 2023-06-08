from datetime import datetime
from turtle import done
import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("habit_tracker.db")
cursor = connection.cursor()

# Create the users table if it doesn't exist
create_table_habits = '''
CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    habit_name TEXT,
    periodicity TEXT,
    type TEXT,
    streak INTEGER,
    start_date DATETIME,
    money_saved INTEGER,
    time_saved INTEGER,
    status TEXT
)
'''
cursor.execute(create_table_habits)

def get_habit_frequency():
    """
    
    """
    print("Select habit frequency:")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    print("4. Yearly")

    while True:
        choice = input("Enter your choice: ")
        if choice in ["1", "2", "3", "4"]:
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    if choice == "1":
        return "Daily"
    elif choice == "2":
        return "Weekly"
    elif choice == "3":
        return "Monthly"
    elif choice == "4":
        return "Yearly"

def break_habit():
    """
    Allows the user to create a negative habit they are looking forward to breaking

    Parameters:
    habit_name (str): The name of the habit
    start_date (int): The date and time of when the user first completed their habti
    periodicity (str): How often does the user plans on doing their habit
    type (str): In which category does the habit fit into
    streak (int): How many times has the user completed their habit consecutively
    money_saved (int): How much money has the user saved by stopping their negative habit
    hourly_wage (int): How much money does the user get payed per hour to calculate the money saved
    time_saved (int): How much time has the user saved by stopping their negative habit
    status (str): Has the habit been comleted in the right timeframe
    """
    habit_name = input("Name your habit!")
    start_date = datetime.now()
    periodicity = get_habit_frequency()

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


