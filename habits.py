from db import insert_predefined_habits, save_new_habit, fetch_habits, update_habit_field, delete_record, fetch_habits_by_type, fetch_habits_by_frequency, fetch_longest_streaks, fetch_longest_streak_for_habit
import pandas as pd
from tabulate import tabulate
from datetime import datetime

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