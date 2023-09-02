from db import insert_predefined_habits, save_new_habit, fetch_habits, update_habit_field, delete_record, fetch_habits_by_type, fetch_habits_by_frequency, fetch_longest_streaks, fetch_longest_streak_for_habit, update_accumulated_fields, update_timer_reset_and_deadline, update_streak, update_status_and_streak, update_status
import pandas as pd
from tabulate import tabulate
from datetime import datetime, timedelta
import random

def predefined_habits(user_id, cursor, connection):
    """
    Inserts predefined habits into the habits table for new users

    Parameters:
    user_id (int): The user's unique id
    predefined_habits (list): A list of dictionaries containing the predefined habits

    Returns:
    none
    """
    predefined_habits_data = [
        {"habit_name": "Meditate", "frequency": "Daily", "habit_type": "Mental and Emotional Well-Being", "money_saved": None, "time_saved": None},
        {"habit_name": "Clean Room", "frequency": "Weekly", "habit_type": "Living and Organization", "money_saved": None, "time_saved": None},
        {"habit_name": "Stop Eating Takeout", "frequency": "Weekly", "habit_type": "Money Wasting", "money_saved": 30, "time_saved": None},
        {"habit_name": "Recycle", "frequency": "Monthly", "habit_type": "Environmental Sustainability", "money_saved": None, "time_saved": None},
        {"habit_name": "Go to the dentist", "frequency": "Yearly", "habit_type": "Health and Fitness", "money_saved": None, "time_saved": None},
    ]
    insert_predefined_habits(user_id, predefined_habits_data, cursor, connection)

def display_habits(user_id, cursor, habit_type=None, frequency=None):
    """
    Displays the user's habits in a table

    Parameters:
    user_id (int): The user's unique id
    habit_type (str, optional): The type of habit to filter by
    frequency (str, optional): The frequency to filter by


    Returns:
    none
    """
    select_query = '''
    SELECT * FROM habits WHERE user_id = ?
    '''
    params = (user_id,)

    if habit_type is not None:
        select_query += " AND habit_type = ?"
        params += (habit_type,)

    if frequency is not None:
        select_query += " AND frequency = ?"
        params += (frequency,)

    cursor.execute(select_query, params)
    habits = cursor.fetchall()

    if not habits:
        print("You have no habits.")
        return
    
    columns = ["Name", "Creation Date", "Frequency", "Habit Type", "Money Saved", 
               "Time Saved", "Last Done", "Streak", "Status"] 
    habit_data = []

    for habit in habits:
        habit_name = habit[2] if habit[2] is not None else ""
        creation_date = habit[3] if habit[3] is not None else ""
        frequency = habit[4] if habit[4] is not None else ""
        habit_type = habit[5] if habit[5] is not None else ""
        accumulated_money_saved = habit[14] if habit[14] is not None else ""
        accumulated_time_saved = habit[15] if habit[15] is not None else ""
        last_done = habit[8] if habit[8] is not None else ""
        streak = habit[9] if habit[9] is not None else ""
        status = habit[11] if habit[11] is not None else ""  

        habit_data.append([habit_name, creation_date, frequency, habit_type, accumulated_money_saved, 
                           accumulated_time_saved, last_done, streak, status])

    habit_df = pd.DataFrame(habit_data, columns=columns)

    # Display the DataFrame as a formatted table
    table = tabulate(habit_df, headers='keys', tablefmt='psql')
    print(table)

def get_habit_name(user_id, cursor):
    """
    Gets the habit name from the user

    Parameters:
    user_id (int): The user's unique id

    Returns:
    habit_name (str): The name of the habit
    """
    habit_name = input("Enter the name of the habit: ")
    select_query = '''
    SELECT * FROM habits WHERE user_id = ? AND habit_name = ?
    '''
    cursor.execute(select_query, (user_id, habit_name))
    habit = cursor.fetchone()
    if habit:
        print("You already have a habit with that name. Please try again.")
        return get_habit_name(user_id, cursor)
    else:
        return habit_name

def get_frequency():
    """
    Gets the frequency of the habit from the user

    Parameters:
    user_id (int): The user's unique id

    Returns:
    frequency (str): The frequency of the habit
    """
    print("Select habit frequency: ")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    print("4. Yearly")
    frequency_input = input("Enter your choice: ")

    if frequency_input == "1":
        frequency_input = "Daily"
    elif frequency_input == "2":
        frequency_input = "Weekly"
    elif frequency_input == "3":
        frequency_input = "Monthly"
    elif frequency_input == "4":
        frequency_input = "Yearly"

    return frequency_input

def get_habit_type_create():
    """
    Allows the user to choose the type of habit they wish to create

    Parameters:
    habit_type (str): The name of the type for the habit

    Returns:
    none
    """
    print("You can choose one of the predifined typer or create your own!")
    print("1. Health and Fitness")
    print("2. Living and Organization")
    print("3. Learning and Personal Development")
    print("4. Relationships and Social Interactions")
    print("5. Mental and Emotional Well-Being")
    print("6. Environmental Sustainability")
    print("7. Other")
    choice = input("Enter your choice:")

    if choice == "1":
        habit_type_input = "Health and Fitness"
    elif choice == "2":
        habit_type_input = "Living and Organization"
    elif choice == "3":
        habit_type_input = "Learning and Personal Development"
    elif choice == "4":
        habit_type_input = "Relationships and Social Interactions"
    elif choice == "5":
        habit_type_input = "Mental and Emotional Well-Being"
    elif choice == "6":
        habit_type_input = "Environmental Sustainability"
    elif choice == "7":
        habit_type_input = input("Write your own type!")

    money_saved_input = None
    time_saved_input = None

    return habit_type_input, money_saved_input, time_saved_input

def get_habit_type_overcome():
    """
    Allows the user to choose the type of habit they wish to overcome

    Parameters:
    habit_type (str): The name of the type for the habit

    Returns:
    none
    """
    print("You can choose one of the predifined typer or create your own!")
    print("1. Time Wasting")
    print("2. Money Wasting")
    print("3. Unhealthy")
    print("4. Other")
    choice = input("Enter your choice:")

    if choice == "1":
        habit_type_input = "Time Wasting"
    elif choice == "2":
        habit_type_input = "Money Wasting"
    elif choice == "3":
        habit_type_input = "Unhealthy"
    elif choice == "4":
        habit_type_input = input("Write your own type!")
    print("Would you like to track how much money you save? ")
    print("1. Yes")
    print("2. No")
   
    choice = input()
    if choice == "1":
        money_saved_input = input("How much money will you save? ")
    elif choice == "2":
        money_saved_input = None  # Set money_saved to None if the user chooses not to track it

    print("Would you like to track how much time you save? ")
    print("1. Yes")
    print("2. No")

    choice = input()
    if choice == "1":
        time_saved_input = input("How much time will you save?(in minutes) ")
    elif choice == "2":
        time_saved_input = None  # Set time_saved to None if the user chooses not to track it
        
    return habit_type_input, money_saved_input, time_saved_input

def create_habits(user_id, cursor, connection):
    """
    Allows the user to create a new habit

    Parameters:
    user_id (int): The user's unique id
    cursor (sqlite3.Cursor): The cursor object to execute SQL queries
    connection (sqlite3.Connection): The connection object to commit changes to the database

    Returns:
    none
    """
    habit_name = get_habit_name(user_id, cursor)
    frequency = get_frequency()
    print("What type of habit would you like to create?")
    print("1. Create a new habit")
    print("2. Overcome a bad habit")
    choice = input("Enter your choice: ")

    if choice == "1":
        habit_type, money_saved, time_saved = get_habit_type_create()
    elif choice == "2":
        habit_type, money_saved, time_saved = get_habit_type_overcome()

    creation_date = datetime.now()
    save_new_habit(user_id, habit_name, creation_date, frequency, habit_type, money_saved, time_saved, cursor)
    connection.commit()
    print("Habit created successfully!")

def display_habits_for_edit(habits):
    """
    Displays the user's habits in a list

    Parameters:
    habits (list): A list of habits

    Returns:
    none
    """
    for index, habit in enumerate(habits):
        print(f"{index + 1}. {habit[2]}")

def get_habit_choice(max_choice, habits):
    """
    Gets the habit choice from the user

    Parameters:
    max_choice (int): The maximum number of choices

    Returns:
    habit_choice (int): The choice of the habit
    """
    habit_choice = int(input("Which habit would you like to edit? "))
    if habit_choice < 1 or habit_choice > len(habits):
        print("Invalid habit choice.")
    return habit_choice

def get_edit_choice():
    """
    Gets the edit choice from the user

    Parameters:
    none

    Returns:
    input (int): The choice of the edit
    """
    print("What would you like to edit? ")
    print("1. Name")
    print("2. Frequency")
    print("3. Habit Type")
    print("4. Money Saved")
    print("5. Time Saved")
    print("6. Exit")
    return input("Enter your choice: ")

def get_new_name():
    """
    Gets the new name for the habit from the user

    Parameters:
    none

    Returns:
    new_name (str): The new name of the habit
    """
    return input("Enter the new name of the habit: ")
    
def get_new_frequency():
    """
    Gets the new frequency for the habit from the user

    Parameters:
    none

    Returns:
    new_frequency (str): The new frequency of the habit
    """
    return get_frequency()

def get_new_habit_type_create():
    """
    Gets the new habit type for the habit from the user

    Parameters:
    none

    Returns:
    new_habit_type (str): The new habit type of the habit
    """
    print("Select a new habit type: ")
    print("1. Health and Fitness")
    print("2. Living and Organization")
    print("3. Learning and Personal Development")
    print("4. Relationships and Social Interactions")
    print("5. Mental and Emotional Well-Being")
    print("6. Environmental Sustainability")
    print("7. Other")
    choice = input("Enter your choice:")

    if choice == "1":
        habit_type_input = "Health and Fitness"
    elif choice == "2":
        habit_type_input = "Living and Organization"
    elif choice == "3":
        habit_type_input = "Learning and Personal Development"
    elif choice == "4":
        habit_type_input = "Relationships and Social Interactions"
    elif choice == "5":
        habit_type_input = "Mental and Emotional Well-Being"
    elif choice == "6":
        habit_type_input = "Environmental Sustainability"
    elif choice == "7":
        habit_type_input = input("Write your own type!")

    return habit_type_input

def get_new_habit_type_overcome():
    """
    Gets the new habit type for the habit from the user

    Parameters:
    none

    Returns:
    new_habit_type (str): The new habit type of the habit
    """
    print("Select a new habit type: ")
    print("1. Time Wasting")
    print("2. Money Wasting")
    print("3. Unhealthy")
    print("4. Other")
    choice = input("Enter your choice:")

    if choice == "1":
        habit_type_input = "Time Wasting"
    elif choice == "2":
        habit_type_input = "Money Wasting"
    elif choice == "3":
        habit_type_input = "Unhealthy"
    elif choice == "4":
        habit_type_input = input("Write your own type!")

    return habit_type_input

def get_new_habit_type():
    """
    Gets the new habit type for the habit from the user

    Parameters:
    none

    Returns:
    new_habit_type (str): The new habit type of the habit
    """
    print("Are you looking to overcome or create a habit?")
    print("1. Create a new habit")
    print("2. Overcome a bad habit")
    choice = input("Enter your choice: ")

    if choice == "1":
        return get_new_habit_type_create()
    elif choice == "2":
        return get_new_habit_type_overcome()

def get_new_money_saved():
    """
    Gets the new money saved for the habit from the user

    Parameters:
    none

    Returns:
    new_money_saved (int): The new money saved of the habit
    """
    return input("Enter the new amount of money saved: ")

def get_new_time_saved():
    """
    Gets the new time saved for the habit from the user

    Parameters:
    none

    Returns:
    new_time_saved (int): The new time saved of the habit
    """
    return input("Enter the new amount of time saved: ")

def edit_habit(user_id, cursor, connection):
    """
    Allows the user to edit their habit

    Parameters:
    user_id (int): The user's unique id
    cursor (sqlite3.Cursor): The cursor object to execute SQL queries
    connection (sqlite3.Connection): The connection object to commit changes to the database

    Returns:
    None
    """
    habits = fetch_habits(user_id, cursor)
    display_habits_for_edit(habits)

    habit_choice = get_habit_choice(len(habits), habits)
    
    selected_habit = habits[habit_choice - 1]
    habit_id = selected_habit[0]

    edit_choice = get_edit_choice()

    if edit_choice == "1":
        new_value = get_new_name()
        update_habit_field("habit_name", new_value, habit_id, cursor)
    elif edit_choice == "2":
        new_value = get_new_frequency()
        update_habit_field("frequency", new_value, habit_id, cursor)
    elif edit_choice == "3":
        new_value = get_new_habit_type()
        update_habit_field("habit_type", new_value, habit_id, cursor)
    elif edit_choice == "4":
        new_value = get_new_money_saved()
        update_habit_field("money_saved", new_value, habit_id, cursor)
    elif edit_choice == "5":
        new_value = get_new_time_saved()
        update_habit_field("time_saved", new_value, habit_id, cursor)
    elif edit_choice == "6":
        return

    connection.commit()

def delete_habit(user_id, cursor, connection):
    """
    Allows the user to delete their habit

    Parameters:
    user_id (int): The user's unique id
    cursor (sqlite3.Cursor): The cursor object to execute SQL queries
    connection (sqlite3.Connection): The connection object to commit changes to the database

    Returns:
    None
    """
    habits = fetch_habits(user_id, cursor)
    display_habits_for_edit(habits)

    habit_choice = get_habit_choice(len(habits), habits)
    selected_habit = habits[habit_choice-1]
    habit_id = selected_habit[0]

    print("Are you sure you want to delete this habit?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your habit has been deleted!")
        delete_record("habits", "habit_id", habit_id, cursor)
        connection.commit()

    elif choice == "2":
        return

def display_statistics_for_type(user_id,cursor):
    """
    Displays the statistics for a specific type of habit

    Parameters:
    user_id (int): The user's unique id
    cursor (sqlite3.Cursor): The cursor object to execute SQL queries

    Returns:
    None
    """
    print("Select a habit type: ")
    print("1. Health and Fitness")
    print("2. Living and Organization")
    print("3. Learning and Personal Development")
    print("4. Relationships and Social Interactions")
    print("5. Mental and Emotional Well-Being")
    print("6. Environmental Sustainability")
    print("7. Time Wasting")
    print("8. Money Wasting")
    print("9. Unhealthy")
    print("10. Other")
    choice = input("Enter your choice: ")

    habit_type_mapping = {
        "1": "Health and Fitness",
        "2": "Living and Organization",
        "3": "Learning and Personal Development",
        "4": "Relationships and Social Interactions",
        "5": "Mental and Emotional Well-Being",
        "6": "Environmental Sustainability",
        "7": "Time Wasting",
        "8": "Money Wasting",
        "9": "Unhealthy",
        "10": "Other"
    }

    habit_type = habit_type_mapping[choice]

    habits = fetch_habits_by_type(user_id, habit_type, cursor)

    if not habits:
        print("You have no habits of this type.")
        return
    else:
        display_habits(user_id, cursor, habit_type=habit_type)

def display_statistics_for_frequency(user_id, cursor):
    """
    Displays the statistics for a specific frequency of habit

    Parameters:
    user_id (int): The user's unique id
    cursor (sqlite3.Cursor): The cursor object to execute SQL queries

    Returns:
    None
    """
    print("Select a habit frequency: ")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    print("4. Yearly")
    choice = input("Enter your choice: ")

    frequency_mapping = {
        "1": "Daily",
        "2": "Weekly",
        "3": "Monthly",
        "4": "Yearly"
    }

    frequency = frequency_mapping[choice]

    habits = fetch_habits_by_frequency(user_id, frequency, cursor)

    if not habits:
        print("You have no habits of this frequency.")
        return
    else:
        display_habits(user_id, cursor, frequency=frequency)

def display_longest_streaks(user_id, cursor):
    """
    Displays the longest streaks for all habits of a given user

    Parameters:
    user_id (int): The user's unique id
    cursor (sqlite3.Cursor): The cursor object to execute SQL queries

    Returns:
    None
    """
    habits = fetch_habits(user_id, cursor)

    if not habits:
        print("You have no habits.")
        return
    else:
        columns = ["Name", "Longest Streak"]
        habit_data = []

        for habit in habits:
            habit_name = habit[2] if habit[2] is not None else ""
            longest_streak = habit[10] if habit[10] is not None else ""

            habit_data.append([habit_name, longest_streak])

        habit_df = pd.DataFrame(habit_data, columns=columns)

        # Display the DataFrame as a formatted table
        table = tabulate(habit_df, headers='keys', tablefmt='psql')
        print(table)

def display_longest_streak_for_habit(user_id, cursor):
    """
    Displays the longest streak for a given habit of a given user

    Parameters:
    user_id (int): The user's unique id
    cursor (sqlite3.Cursor): The cursor object to execute SQL queries

    Returns:
    None
    """
    habits = fetch_habits(user_id, cursor)

    if not habits:
        print("You have no habits.")
        return
    else:
        display_habits_for_edit(habits)

        habit_choice = get_habit_choice(len(habits), habits)
        selected_habit = habits[habit_choice-1]
        habit_id = selected_habit[0]

        habit_name = selected_habit[2] if selected_habit[2] is not None else ""
        longest_streak = selected_habit[10] if selected_habit[10] is not None else ""

        print(f"{habit_name}: {longest_streak}")

def statistics(user_id, cursor, connection):
    """
    Displays the statistics for a specific type of habit

    Parameters:
    user_id (int): The user's unique id
    cursor (sqlite3.Cursor): The cursor object to execute SQL queries

    Returns:
    None
    """
    print("What would you like to do?")
    print("1. View statistics for a specific type of habit")
    print("2. View statistics for a specific frequency of habit")
    print("3. View the longest streaks for all habits")
    print("4. View the longest streak for a specific habit")
    choice = input("Enter your choice: ")

    if choice == "1":
        display_statistics_for_type(user_id, cursor)
    elif choice == "2":
        display_statistics_for_frequency(user_id, cursor)
    elif choice == "3":
        display_longest_streaks(user_id, cursor)
    elif choice == "4":
        display_longest_streak_for_habit(user_id, cursor)

def calculate_timer_reset(cursor, habit_id):
    """
    Calculates the next allowed completion time based on the frequency of the habit

    Parameters:
    cursor (sqlite3.Cursor): The SQLite cursor
    habit_id (int): The ID of the habit

    Returns:
    datetime: The calculated next completion time
    """
    select_query = '''
    SELECT frequency FROM habits WHERE habit_id = ?
    '''
    cursor.execute(select_query, (habit_id,))
    habit = cursor.fetchone()

    frequency = habit[0]

    current_datetime = datetime.now()

    if frequency == "Daily":
        timer_reset = current_datetime.replace(hour=23, minute=59, second=59, microsecond=99999)
    elif frequency == "Weekly":
        days_until_next_sunday = (6 - current_datetime.weekday()) % 7
        next_sunday = current_datetime + timedelta(days=days_until_next_sunday)
        timer_reset = next_sunday.replace(hour=23, minute=59, second=59, microsecond=99999)
    elif frequency == "Monthly":
        next_month = current_datetime.month + 1 if current_datetime.month < 12 else 1
        next_year = current_datetime.year if next_month > current_datetime.month else current_datetime.year + 1
        next_month_first_day = current_datetime.replace(year=next_year, month=next_month, day=1,
                                                        hour=0, minute=0, second=0, microsecond=0)
        timer_reset = next_month_first_day - timedelta(microseconds=1)
    elif frequency == "Yearly":
        next_year_first_day = current_datetime.replace(year=current_datetime.year + 1, month=1, day=1,
                                                      hour=0, minute=0, second=0, microsecond=0)
        timer_reset = next_year_first_day - timedelta(microseconds=1)
    else:
        print("Invalid frequency.")
        return None
    
    return timer_reset

def calculate_deadline(cursor, habit_id):
    """
    Calculates the deadline for the habit based on the frequency

    Parameters:
    cursor (sqlite3.Cursor): The SQLite cursor
    habit_id (int): The ID of the habit

    Returns:
    deadline (datetime): The calculated deadline
    """
    select_query = '''
    SELECT frequency FROM habits WHERE habit_id = ?
    '''
    cursor.execute(select_query, (habit_id,))
    habit = cursor.fetchone()

    frequency = habit[0]
    current_datetime = datetime.now()

    if frequency == "Daily":
        deadline = current_datetime + timedelta(days=1)
        deadline = deadline.replace(hour=23, minute=59, second=59, microsecond=99999)
    elif frequency == "Weekly":
        days_until_next_sunday = (6 - current_datetime.weekday()) % 7
        next_sunday = current_datetime + timedelta(days=days_until_next_sunday + 7)
        deadline = next_sunday.replace(hour=23, minute=59, second=59, microsecond=99999)
    elif frequency == "Monthly":
        next_month = current_datetime.month + 2 if current_datetime.month < 12 else 1
        next_year = current_datetime.year if next_month > current_datetime.month else current_datetime.year + 1
        next_month_first_day = current_datetime.replace(year=next_year, month=next_month, day=1,
                                                        hour=0, minute=0, second=0, microsecond=0)
        deadline = next_month_first_day - timedelta(microseconds=1)
    elif frequency == "Yearly":
        deadline = current_datetime.replace(year=current_datetime.year + 1, month=12, day=31,
                                            hour=23, minute=59, second=59, microsecond=99999)
    else:
        deadline = None

    return deadline

def mark_habit_done(user_id, cursor, connection):
    """
    Marks a habit as done

    Parameters:
    user_id (int): The user's unique id
    cursor (sqlite3.Cursor): The SQLite cursor
    connection (sqlite3.Connection): The connection object to commit changes to the database

    Returns:
    None
    """
    habits = fetch_habits(user_id, cursor)
    for index, habit in enumerate(habits):
        print(f"{index + 1}. {habit[2]}")

    habit_choice = int(input("Which habit would you like to mark as done? "))
    if habit_choice < 1 or habit_choice > len(habits):
        print("Invalid habit choice.")
        return
    else:
        selected_habit = habits[habit_choice-1]
        habit_id = selected_habit[0]
        habit_name = selected_habit[2]
        frequency = selected_habit[4]
        status = selected_habit[11]
        accumulated_money_saved = selected_habit[14]
        accumulated_time_saved = selected_habit[15]
        timer_reset = selected_habit[12]

        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if timer_reset is not None and current_datetime < timer_reset:
            print("This habit isn't due yet!")
            display_habits(user_id, cursor)

        else:
            money_saved = selected_habit[6]
            time_saved = selected_habit[7]

            # Update accumulated_money_saved and accumulated_time_saved
            update_accumulated_fields(cursor, habit_id, money_saved, time_saved)
                
            # Update last_done and status
            update_habit_field("last_done", current_datetime, habit_id, cursor)
            update_habit_field("status", "Done", habit_id, cursor)

            # Update timer_reset and deadline
            timer_reset = calculate_timer_reset(cursor, habit_id)
            deadline = calculate_deadline(cursor, habit_id)
            update_timer_reset_and_deadline(cursor, habit_id, timer_reset, deadline)

            connection.commit()

            print(f"Congratulations! You've completed the habit '{habit_name}'.")
            return habit_id

def calculate_and_update_streak(habit_id, cursor, connection):
    """
    Calculates the streak of a habit and updates it in the database

    Parameters:
    habit_id (int): The ID of the habit
    cursor (sqlite3.Cursor): The SQLite cursor
    connection (sqlite3.Connection): The connection object to commit changes to the database

    Returns:
    int: The streak of the habit
    """
    select_query = '''
    SELECT * FROM habits WHERE habit_id = ?
    '''
    cursor.execute(select_query, (habit_id,))
    habit = cursor.fetchone()

    last_done = habit[8]
    streak = habit[9]
    longest_streak = habit[10]
    status = habit[11]
    timer_reset = habit[12]

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if status == "Done":
        if last_done is not None and timer_reset is not None:
            last_done_datetime = datetime.strptime(last_done, "%Y-%m-%d %H:%M:%S")
            timer_reset_datetime = datetime.strptime(timer_reset, "%Y-%m-%d %H:%M:%S.%f")

            if current_datetime <= timer_reset:
                streak = streak + 1 if streak is not None else 1
                print("You're on a streak!")
            else:
                streak = 0
                print("You broke your streak!")
            
            update_streak(cursor, habit_id, streak)
            
            if streak > (habit[10] or 0):
                longest_streak = streak
                update_habit_field("longest_streak", streak, habit_id, cursor)

            connection.commit()
    else:
        streak = 0
        update_streak(cursor, habit_id, streak)
        connection.commit()

    return streak, longest_streak

def encouraging_message(user_id, habit_id, cursor):
    """
    Displays an encouraging message to the user after achieving a streak of 5 and in intervals of 5 after that

    Parameters:
    habit_id (int): The ID of the habit
    cursor (sqlite3.Cursor): The SQLite cursor

    Returns:
    None
    """
    encouraging_messages = [
        "You can do it!",
        "Keep going!",
        "You're doing great!",
        "Don't give up!",
        "You're on a roll!",
        "Congratulations on your streak! Keep up the great work!",
        "Way to go! You're building a powerful habit.",
        "You're on fire! Keep that momentum going.",
        "You're unstoppable! Nothing can break your streak now.",
        "Awesome job! Your dedication is inspiring.",
        "You're making progress every day. Keep it up!",
        "Keep going, you're on the right track!",
        "You're proving that consistency is the key to success.",
        "Keep showing up for yourself, and great things will happen.",
        "You're doing it! Keep those positive habits going strong.",
        "Your streak is a testament to your commitment and determination.",
        "You're a streak superstar! Keep shining brightly.", 
        "You're making positive changes, one day at a time.",
        "You're forming habits that will change your life for the better.",
        "You're building a foundation for success with each new day.",
        "Each day you keep your streak alive, you're growing stronger.",
        "Way to stick with it! Your progress is remarkable.",
        "You're proving that small steps lead to big results.",
        "Every day counts, and you're making the most of each one.",
        "You're showing incredible discipline and focus. Keep it up!",
        "Keep celebrating those wins. You're doing amazing!",
        "You're proving that consistency pays off in a big way.",
        "You're a streak master! Keep that streak alive and thriving.",
        "You're turning your aspirations into accomplishments.",
        "You're becoming the best version of yourself. Keep it up!",
        "You've got this! One day at a time, you're achieving greatness."
    ]

    encouraging_message = random.choice(encouraging_messages)	

    select_query = '''
    SELECT * FROM habits WHERE habit_id = ?
    '''
    cursor.execute(select_query, (habit_id,))
    habit = cursor.fetchone()

    streak = habit[9]

    if streak is not None and streak > 0 and streak % 5 == 0:
        print(encouraging_message)
        return

def update_habit_status(user_id, cursor, connection):
    habits = fetch_habits(user_id, cursor)

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for habit in habits:
        habit_id, habit_name, status, timer_reset, deadline, streak = habit[0], habit[2], habit[11], habit[12], habit[13], habit[9]
        
        if deadline and current_datetime >= deadline:
            update_status_and_streak(cursor, connection, habit_id, None, 0)
            print(f"The streak for habit '{habit_name}' has been broken due to passing the deadline.")

        elif deadline and current_datetime < deadline:
            if status == "Done" and current_datetime >= timer_reset:
                update_status(cursor, connection, habit_id, "Not Done")
                print(f"Habit '{habit_name}' is now due for completion!")

            elif status == "Not Done" and current_datetime >= timer_reset:
                update_status_and_streak(cursor, connection, habit_id, None, 0)
                print(f"The streak for habit '{habit_name}' has been reset.")