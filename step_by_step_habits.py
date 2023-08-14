import sqlite3
from datetime import datetime, timedelta
import pandas as pd
from tabulate import tabulate
import random

# Connect to the SQLite database
connection = sqlite3.connect("habit_tracker.db")
cursor = connection.cursor()

create_table_habits = '''
CREATE TABLE IF NOT EXISTS habits (
    habit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    habit_name TEXT,
    start_date DATETIME,
    frequency TEXT,
    habit_type TEXT,
    money_saved INTEGER,
    time_saved INTEGER,
    last_done DATETIME,
    streak INTEGER,
    status TEXT,
    timer_reset DATETIME,
    deadline DATETIME,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
)
'''
cursor.execute(create_table_habits)    

def predefined_habits(user_id):
    """
    Gives the user 5 predefined habits to start off with

    Parameters:
    user_id (int): The ID of the user

    Returns:
    None
    """
    predefined_habits = [
        {"habit_name": "Meditate", "frequency": "Daily", "habit_type": "Mental and Emotional Well-Being", "money_saved": None, "time_saved": None},
        {"habit_name": "Clean Room", "frequency": "Weekly", "habit_type": "Living and Organization", "money_saved": None, "time_saved": None},
        {"habit_name": "Stop eating takeout", "frequency": "Weekly", "habit_type": "Money Wasting", "money_saved": 30, "time_saved": None},
        {"habit_name": "Recycle", "frequency": "Monthly", "habit_type": "Environmental Sustainability", "money_saved": None, "time_saved": None},
        {"habit_name": "Go to the dentist", "frequency": "Yearly", "habit_type": "Health and Fitness", "money_saved": None, "time_saved": None}
    ]

    # Insert the predefined habits into the habits table
    insert_data = '''
    INSERT INTO habits (user_id, habit_name, frequency, habit_type, money_saved, time_saved, status, start_date, last_done, streak)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    for habit in predefined_habits:
        cursor.execute(insert_data, (user_id, habit["habit_name"], habit["frequency"], habit["habit_type"],
                                     habit["money_saved"], habit["time_saved"], None, None, None, None))

    connection.commit()

def habit_name():
    """
    Allows the user to create a name for their habit

    Parameters:
    name (str): The name of the habit

    Returns:
    none
    """
    habit_name_input = input("Name your habit! ")

    print("The name of your habit is", habit_name_input, "is that correct?")
    print("1. Yes")
    print("2. No")

    choice = input()

    if choice == "1":
        print("Perfect!")
        return habit_name_input

    elif choice == "2":
        return habit_name()

def update_name(habit_id):
    """
    Allows the user to update the name of a habit

    Parameters:
    habit_id (int): The ID of the habit

    Returns:
    None
    """

    habit_name_input = input("Enter the new name for the habit: ")

    # Update the habit name in the habits table
    update_query = '''
    UPDATE habits SET habit_name = ? WHERE habit_id = ?
    '''
    cursor.execute(update_query, (habit_name_input, habit_id,))
    connection.commit()

    print("Habit name has been updated successfully!")
    return habit_name_input

def frequency():
    """
    Allows the user to select the frequency with which they wish to maintain the habit

    Parameters:
    choice (str): What the user chose as the frequency for the desired habit

    Returns:
    none
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

    print("Your frequency is", frequency_input, "is that correct?")
    print("1. Yes")
    print("2. No")

    choice = input()
    if choice == "1":
        print("Perfect!")
        return frequency_input
                
    elif choice == "2":
        return frequency()

def update_frequency(habit_id):
    """
    Allows the user to update the frequency of a habit

    Parameters:
    habit_id (int): The ID of the habit

    Returns:
    None
    """

    print("Select a new habit frequency: ")
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

    # Update the frequency in the habits table
    update_query = '''
    UPDATE habits SET frequency = ? WHERE habit_id = ?
    '''
    cursor.execute(update_query, (frequency_input, habit_id,))
    connection.commit()

    print("Habit frequency has been updated successfully!")
    return frequency_input

def overcome_habit():
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

    print("Your type is", habit_type_input, "is that correct?")
    print("1. Yes")
    print("2. No")

    choice = input()
    if choice == "1":
        print("Perfect!")

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

    elif choice == "2":
        return overcome_habit()

def update_overcome_habit(habit_id):
    """
    Allows the user to update the type of a habit

    Parameters:
    habit_id (int): The ID of the habit

    Returns:
    None
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

    # Update the habit type in the habits table
    update_query = '''
    UPDATE habits SET habit_type = ? WHERE habit_id = ?
    '''
    cursor.execute(update_query, (habit_type_input, habit_id,))
    connection.commit()

    print("Habit type has been updated successfully!")
    return habit_type_input

def create_habit():
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
            
    print("Your type is", habit_type_input, "is that correct?")
    print("1. Yes")
    print("2. No")

    choice = input()
    if choice == "1":
        money_saved_input = None
        time_saved_input = None
        print("Perfect!")
        return habit_type_input, money_saved_input, time_saved_input

    elif choice == "2":
        return create_habit()

def update_create_habit(habit_id):
    """
    Allows the user to update the type of a habit

    Parameters:
    habit_id (int): The ID of the habit

    Returns:
    None
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

    # Update the habit type in the habits table
    update_query = '''
    UPDATE habits SET habit_type = ? WHERE habit_id = ?
    '''
    cursor.execute(update_query, (habit_type_input, habit_id,))
    connection.commit()

    print("Habit type has been updated successfully!")
    return habit_type_input

def update_money_saved(habit_id):
    """
    Allows the user to update the money saved of a habit

    Parameters:
    habit_id (int): The ID of the habit

    Returns:
    None
    """

    money_saved_input = input("How much money will you save? ")

    # Update the money saved in the habits table
    update_query = '''
    UPDATE habits SET money_saved = ? WHERE habit_id = ?
    '''
    cursor.execute(update_query, (money_saved_input, habit_id,))
    connection.commit()

    print("Money saved has been updated successfully!")
    return money_saved_input

def update_time_saved(habit_id):
    """
    Allows the user to update the time saved of a habit

    Parameters:
    habit_id (int): The ID of the habit

    Returns:
    None
    """

    time_saved_input = input("How much time will you save?(in minutes) ")

    # Update the time saved in the habits table
    update_query = '''
    UPDATE habits SET time_saved = ? WHERE habit_id = ?
    '''
    cursor.execute(update_query, (time_saved_input, habit_id,))
    connection.commit()

    print("Time saved has been updated successfully!")
    return time_saved_input
        
def save_habit(habit_name_input, frequency_input, habit_type_input, money_saved_input, time_saved_input, user_id):
    """
    Saves the habit information into the table of habits

    Parameters:
    habit_name_input (str): The name of the habit
    frequency_input (str): The frequency of the habit
    habit_type_input (str): The type of the habit

    Returns:
    none
    """
    # Insert the habit into the habits table
    insert_data = '''
    INSERT INTO habits (user_id, habit_name, frequency, habit_type, money_saved, time_saved, status, start_date, last_done, streak)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(insert_data, (user_id, habit_name_input, frequency_input, habit_type_input, money_saved_input, time_saved_input, None, None, None, None))
    connection.commit()

def display_habits(user_id):
    """
    Displays a table with all the habits of the user

    Parameters:
    user_id (int): The ID of the user

    Returns:
    None
    """
    select_query = '''
    SELECT * FROM habits WHERE user_id = ?
    '''
    cursor.execute(select_query, (user_id,))
    habits = cursor.fetchall()

    # Create a DataFrame from the habits data
    columns = ["Name", "Start Date", "Frequency", "Habit Type", "Money Saved", 
    "Time Saved", "Last Done", "Streak", "Status"]
    habit_data = []
    for habit in habits:
        # Check for None values and substitute with an empty string or placeholder
        habit_name = habit[2] if habit[2] is not None else ""
        start_date = habit[3] if habit[3] is not None else ""
        frequency = habit[4] if habit[4] is not None else ""
        habit_type = habit[5] if habit[5] is not None else ""
        money_saved = habit[6] if habit[6] is not None else ""
        time_saved = habit[7] if habit[7] is not None else ""
        last_done = habit[8] if habit[8] is not None else ""
        streak = habit[9] if habit[9] is not None else ""
        status = habit[10] if habit[10] is not None else ""

        habit_data.append([habit[2], habit[3], habit[4], habit[5], habit[6], habit[7], 
        habit[8], habit[9], habit[10]])

    habit_df = pd.DataFrame(habit_data, columns=columns)

    # Display the DataFrame as a formatted table
    table = tabulate(habit_df, headers='keys', tablefmt='psql')
    print(table)

def create_habits(user_id):
    """
    Displays a table with all the habits of the user

    Parameters:
    user_id (int): The ID of the user

    Returns:
    None
    """
    select_query = '''
    SELECT * FROM habits WHERE user_id = ?
    '''
    cursor.execute(select_query, (user_id,))
    habits = cursor.fetchall()

    habit_name_input = habit_name()
    frequency_input = frequency()
    print("Are you looking to overcome or create a habit?")
    print("1. Overcome a habit")
    print("2. Create a habit")
    choice = input("Enter your choice: ")
    if choice == "1":
    	habit_type_input, money_saved_input, time_saved_input = overcome_habit()
    elif choice == "2":
        habit_type_input, money_saved_input, time_saved_input = create_habit()

    print("Your habit has been created!")
    print("Here's a summary of your habit:")
    print("Habit name:", habit_name_input)
    print("Frequency:", frequency_input)
    print("Habit type:", habit_type_input)

    # Save the habit information into the table of habits
    save_habit(habit_name_input, frequency_input, habit_type_input, money_saved_input, 
    time_saved_input, user_id)

    return habit_name_input, frequency_input, habit_type_input, money_saved_input, time_saved_input, user_id

def edit_habit(user_id):
    """
    Allows the user to edit their habit

    Parameters:
    habit_id (int): The ID of the habit

    Returns:
    None
    """

    select_query = '''
    SELECT * FROM habits WHERE user_id = ?
    '''
    cursor.execute(select_query, (user_id,))
    habits = cursor.fetchall()
    
    for index, habit in enumerate(habits):
        print(f"{index+1}. {habit[2]}")

    habit_choice = int(input("Which habit would you like to edit? "))
    if habit_choice < 1 or habit_choice > len(habits):
        print("Invalid habit choice.")
    else:
        selected_habit = habits[habit_choice-1]
        habit_id = selected_habit[0]
        habit_name = selected_habit[2]
        frequency = selected_habit[4]
        habit_type = selected_habit[5]
        money_saved = selected_habit[6]
        time_saved = selected_habit[7]
        last_done = selected_habit[8]

    print("What would you like to edit? ")
    print("1. Name")
    print("2. Frequency")
    print("3. Habit Type")
    print("4. Money Saved")
    print("5. Time Saved")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        habit_name_input = update_name(habit_id)
        print("Your habit has been updated!")
        print("Here's a summary of your habit:")
        print("Habit name:", habit_name_input)
        print("Frequency:", frequency)
        print("Habit type:", habit_type)

        # Update the habit information into the table of habits
        update_data = '''
        UPDATE habits SET habit_name = ? WHERE habit_id = ?
        '''
        cursor.execute(update_data, (habit_name_input, habit_id,))
        connection.commit()

        select_query = '''
        SELECT * FROM habits WHERE user_id = ? AND habit_id = ?
        '''
        cursor.execute(select_query, (user_id, habit_id,))
        habits = cursor.fetchall()
        return habits

    elif choice == "2":
        frequency_input = update_frequency(habit_id)
        print("Your habit has been updated!")
        print("Here's a summary of your habit:")
        print("Habit name:", habit_name)
        print("Frequency:", frequency_input)
        print("Habit type:", habit_type)

        # Update the habit information into the table of habits
        update_data = '''
        UPDATE habits SET frequency = ? WHERE habit_id = ?
        '''
        cursor.execute(update_data, (frequency_input, habit_id,))
        connection.commit()

        select_query = '''
        SELECT * FROM habits WHERE user_id = ? AND habit_id = ?
        '''
        cursor.execute(select_query, (user_id, habit_id,))
        habits = cursor.fetchall()
        return habits

    elif choice == "3":
        print("Are you looking to overcome or create a habit?")
        print("1. Overcome a habit")
        print("2. Create a habit")
        choice = input("Enter your choice: ")
        if choice == "1":
            habit_type_input = update_overcome_habit(habit_id)
        elif choice == "2":
            habit_type_input = update_create_habit(habit_id)
        print("Your habit has been updated!")
        print("Here's a summary of your habit:")
        print("Habit name:", habit_name)
        print("Frequency:", frequency)
        print("Habit type:", habit_type_input)

        # Update the habit information into the table of habits
        update_data = '''
        UPDATE habits SET habit_type = ? WHERE habit_id = ?
        '''
        cursor.execute(update_data, (habit_type_input, habit_id,))
        connection.commit()

        select_query = '''
        SELECT * FROM habits WHERE user_id = ? AND habit_id = ?
        '''
        cursor.execute(select_query, (user_id, habit_id,))
        habits = cursor.fetchall()
        return habits

    elif choice == "4":
        money_saved_input = input("How much money will you save? ")
        print("Your habit has been updated!")
        print("Here's a summary of your habit:")
        print("Habit name:", habit_name)
        print("Habit type:", habit_type)
        print("Money saved:", money_saved_input)
        print("Time saved:", time_saved)

        # Update the habit information into the table of habits
        update_data = '''
        UPDATE habits SET money_saved = ? WHERE habit_id = ?
        '''
        cursor.execute(update_data, (money_saved_input, habit_id,))
        connection.commit()

        select_query = '''
        SELECT * FROM habits WHERE user_id = ? AND habit_id = ?
        '''
        cursor.execute(select_query, (user_id, habit_id,))
        habits = cursor.fetchall()
        return habits

    elif choice == "5":
        time_saved_input = input("How much time will you save?(in minutes) ")
        print("Your habit has been updated!")
        print("Here's a summary of your habit:")
        print("Habit name:", habit_name)
        print("Habit type:", habit_type)
        print("Money saved:", money_saved)
        print("Time saved:", time_saved_input)

        # Update the habit information into the table of habits
        update_data = '''
        UPDATE habits SET time_saved = ? WHERE habit_id = ?
        '''
        cursor.execute(update_data, (time_saved_input, habit_id,))
        connection.commit()

        select_query = '''
        SELECT * FROM habits WHERE user_id = ? AND habit_id = ?
        '''
        cursor.execute(select_query, (user_id, habit_id,))
        habits = cursor.fetchall()
        return habits
            
    elif choice == "6":
        what_to_do_now(user_id)  

def delete_habit(user_id):
    """
    Allows the user to delete their habit

    Parameters:
    habit_id (int): The ID of the habit

    Returns:
    None
    """

    select_query = '''
    SELECT * FROM habits WHERE user_id = ?
    '''
    cursor.execute(select_query, (user_id,))
    habits = cursor.fetchall()
    
    for index, habit in enumerate(habits):
        print(f"{index+1}. {habit[2]}")

    habit_choice = int(input("Which habit would you like to delete? "))
    if habit_choice < 1 or habit_choice > len(habits):
        print("Invalid habit choice.")
    else:
        selected_habit = habits[habit_choice-1]
        habit_id = selected_habit[0]
        habit_name = selected_habit[2]
        frequency = selected_habit[4]
        habit_type = selected_habit[5]
        money_saved = selected_habit[6]
        time_saved = selected_habit[7]
        last_done = selected_habit[8]

    print("Are you sure you want to delete this habit?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your habit has been deleted!")

        # Delete the habit information from the table of habits
        delete_data = '''
        DELETE FROM habits WHERE habit_id = ?
        '''
        cursor.execute(delete_data, (habit_id,))
        connection.commit()

        select_query = '''
        SELECT * FROM habits WHERE user_id = ? AND habit_id = ?
        '''
        cursor.execute(select_query, (user_id, habit_id,))
        habits = cursor.fetchall()
        return habits

    elif choice == "2":
        what_to_do_now(user_id)

def statistics(user_id):
    """
    Allows the user to view statistics about their habits

    Parameters:
    user_id (int): The ID of the user

    Returns:
    None
    """
    print("What would you like to view statistics for?")
    print("1. All habits with a specific habit type")
    print("2. All habits with a specific frequency")
    print("3. Longest run streak for all habits")
    print("4. Longest run streak for a habit")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
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

        select_query = '''
        SELECT * FROM habits WHERE user_id = ? AND habit_type = ?
        '''
        cursor.execute(select_query, (user_id, habit_type,))
        habits = cursor.fetchall()

        # Create a DataFrame from the habits data
        columns = ["Name", "Start Date", "Frequency", "Habit Type", "Money Saved", 
        "Time Saved", "Last Done", "Streak", "Status"]
        habit_data = []
        for habit in habits:
            # Check for None values and substitute with an empty string or placeholder
            habit_name = habit[2] if habit[2] is not None else ""
            start_date = habit[3] if habit[3] is not None else ""
            frequency = habit[4] if habit[4] is not None else ""
            habit_type = habit[5] if habit[5] is not None else ""
            money_saved = habit[6] if habit[6] is not None else ""
            time_saved = habit[7] if habit[7] is not None else ""
            last_done = habit[8] if habit[8] is not None else ""
            streak = habit[9] if habit[9] is not None else ""
            status = habit[10] if habit[10] is not None else ""

            habit_data.append([habit[2], habit[3], habit[4], habit[5], habit[6], habit[7], 
            habit[8], habit[9], habit[10]])

        habit_df = pd.DataFrame(habit_data, columns=columns)

        # Display the DataFrame as a formatted table
        table = tabulate(habit_df, headers='keys', tablefmt='psql')
        print(table)
        
    elif choice == "2":
        print("Select a frequency: ")
        print("1. Daily")
        print("2. Weekly")
        print("3. Monthly")
        print("4. Yearly")
        choice = input("Enter your choice: ")

        frequency_mapping = {
            "1": "daily",
            "2": "weekly",
            "3": "monthly",
            "4": "yearly"
        }

        frequency = frequency_mapping[choice]

        select_query = '''
        SELECT * FROM habits WHERE user_id = ? AND frequency = ?
        '''
        cursor.execute(select_query, (user_id, frequency,))
        habits = cursor.fetchall()

        # Create a DataFrame from the habits data
        columns = ["Name", "Start Date", "Frequency", "Habit Type", "Money Saved",
        "Time Saved", "Last Done", "Streak", "Status"]
        habit_data = []
        for habit in habits:
            # Check for None values and substitute with an empty string or placeholder
            habit_name = habit[2] if habit[2] is not None else ""
            start_date = habit[3] if habit[3] is not None else ""
            frequency = habit[4] if habit[4] is not None else ""
            habit_type = habit[5] if habit[5] is not None else ""
            money_saved = habit[6] if habit[6] is not None else ""
            time_saved = habit[7] if habit[7] is not None else ""
            last_done = habit[8] if habit[8] is not None else ""
            streak = habit[9] if habit[9] is not None else ""
            status = habit[10] if habit[10] is not None else ""

            habit_data.append([habit[2], habit[3], habit[4], habit[5], habit[6], habit[7],
            habit[8], habit[9], habit[10]])

        habit_df = pd.DataFrame(habit_data, columns=columns)

        # Display the DataFrame as a formatted table
        table = tabulate(habit_df, headers='keys', tablefmt='psql')
        print(table)
    elif choice == "3":
        select_query = '''
        SELECT habit_name, MAX(streak) as longest_streak 
        FROM habits 
        WHERE user_id = ?
        GROUP BY habit_name
        '''
        cursor.execute(select_query, (user_id,))
        longest_streaks = cursor.fetchall()

        # Create a DataFrame from the habits data
        columns = ["Name", "Longest Streak"]
        streak_data = []
        for streak in longest_streaks:
            # Check for None values and substitute with an empty string or placeholder
            habit_name = streak[0] if streak[0] is not None else ""
            longest_streak = streak[1] if streak[1] is not None else ""

            streak_data.append([streak[0], streak[1]])

        streak_df = pd.DataFrame(streak_data, columns=columns)

        # Display the DataFrame as a formatted table
        table = tabulate(streak_df, headers='keys', tablefmt='psql')
        print(table)
    elif choice == "4":
        select_query = '''
        SELECT * FROM habits WHERE user_id = ?
        '''
        cursor.execute(select_query, (user_id,))
        habits = cursor.fetchall()

        for index, habit in enumerate(habits):
            print(f"{index+1}. {habit[2]}")

        habit_choice = int(input("Which habit would you like to view the longest streak for? "))
        if habit_choice < 1 or habit_choice > len(habits):
            print("Invalid habit choice.")
        else:
            selected_habit = habits[habit_choice-1]
            habit_id = selected_habit[0]
            habit_name = selected_habit[2]
            frequency = selected_habit[4]
            habit_type = selected_habit[5]
            money_saved = selected_habit[6]
            time_saved = selected_habit[7]
            last_done = selected_habit[8]

        select_query = '''
        SELECT MAX(streak) FROM habits WHERE habit_id = ?
        '''
        cursor.execute(select_query, (habit_id,))
        longest_streak = cursor.fetchone()[0]

        print(f"The longest streak for {habit_name} is {longest_streak}!")
    elif choice == "5":
        what_to_do_now(user_id)

def start_date(habit_id):
    """
    Allows the user to track their starting date as soon as they mark a habit as "done" for the first time

    Parameters:
    start_date (datetime): The date the user started the habit

    Returns:
    none
    """
    if status == "Done":
        start_date_input = datetime.now()
            
        insert_data = '''
        INSERT INTO habits (start_date, user_id)
        VALUES (?, ?)
        '''
        cursor.execute(insert_data, (start_date_input, user_id,))
        connection.commit()
    else:
        None

def last_done(habit_id):
    """
    Allows the user to track the last time they marked a habit as "done"

    Parameters:
    last_done (datetime): The date the user last did the habit

    Returns:
    none
    """
    if status == "Done":
        last_done_input = datetime.now()

        insert_data = '''
        INSERT INTO habits (last_done, habit_id)
        VALUES (?, ?)
        '''
        cursor.execute(insert_data, (last_done_input, habit_id,))
        connection.commit()
    else:
        None

def calculate_timer_reset(habit_id):
    """
    Calculates the next allowed completion time based on the frequency of the habit

    Parameters:
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
        timer_reset = current_datetime.replace(hour=23, minute=59, second=59, microsecond=999)
    elif frequency == "Weekly":
        days_until_next_sunday = (6 - current_datetime.weekday()) % 7
        next_sunday = current_datetime + timedelta(days=days_until_next_sunday)
        timer_reset = next_sunday.replace(hour=23, minute=59, second=59, microsecond=999)
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

def calculate_deadline(habit_id):
    """
    Calculates the deadline for the habit based on the frequency

    Parameters:
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
        next_day = current_datetime.day + 1 if current_datetime.day < 31 else 1
        deadline = current_datetime.replace(day=next_day, hour=23, minute=59, second=59, microsecond=999)
    elif frequency == "Weekly":
        days_until_next_sunday = (6 - current_datetime.weekday()) % 7
        next_sunday = current_datetime + timedelta(days=days_until_next_sunday + 7)
        deadline = next_sunday.replace(hour=23, minute=59, second=59, microsecond=999)
    elif frequency == "Monthly":
        next_month = current_datetime.month + 2 if current_datetime.month < 12 else 1
        next_year = current_datetime.year if next_month > current_datetime.month else current_datetime.year + 1
        next_month_first_day = current_datetime.replace(year=next_year, month=next_month, day=1,
                                                        hour=0, minute=0, second=0, microsecond=0)
        deadline = next_month_first_day - timedelta(microseconds=1)
    elif frequency == "Yearly":
        deadline = current_datetime.replace(year=current_datetime.year + 1, month=12, day=31,
                                            hour=23, minute=59, second=59, microsecond=999)
    else:
        deadline = None

    return deadline

def update_timer_reset(habit_id, timer_reset):
    """
    Updates the next completion time of a habit

    Parameters:
    habit_id (int): The ID of the habit
    timer_reset (datetime): The next completion time of the habit

    Returns:
    None
    """
    update_next_completion_query = '''
    UPDATE habits SET timer_reset = ? WHERE habit_id = ?
    '''
    cursor.execute(update_next_completion_query, (timer_reset, habit_id,))
    connection.commit()

def update_deadline(habit_id, deadline):
    """
    Updates the deadline of a habit

    Parameters:
    habit_id (int): The ID of the habit
    deadline (datetime): The deadline of the habit

    Returns:
    None
    """
    update_deadline_query = '''
    UPDATE habits SET deadline = ? WHERE habit_id = ?
    '''
    cursor.execute(update_deadline_query, (deadline, habit_id,))
    connection.commit()

def mark_habit_done(user_id):
    """
    Marks a habit as done for the current date

    Parameters:
    user_id (int): The ID of the user

    Returns:
    None
    """
    select_query = '''
    SELECT * FROM habits WHERE user_id = ?
    '''
    cursor.execute(select_query, (user_id,))
    habits = cursor.fetchall()

    # Display the habits to choose from
    for index, habit in enumerate(habits):
        print(f"{index+1}. {habit[2]}")

    habit_choice = int(input("Which habit would you like to mark as done? "))
    if habit_choice < 1 or habit_choice > len(habits):
        print("Invalid habit choice.")
        what_to_do_now(user_id)
    else:
        selected_habit = habits[habit_choice-1]
        habit_id = selected_habit[0]
        habit_name = selected_habit[2]
        frequency = selected_habit[4]
        status = selected_habit[10]

        # Get the current date and time
        current_datetime = datetime.now()

        if status is None or status == "Not Done":
            # Calculate the next allowed completion time based on frequency
            if frequency == "Daily":
                timer_reset = current_datetime + timedelta(days=1)
                timer_reset = timer_reset.replace(hour=0, minute=1, second=0, microsecond=0)
            elif frequency == "Weekly":
                days_until_next_weekday = (6 - current_datetime.weekday()) % 7
                timer_reset = current_datetime + timedelta(days=days_until_next_weekday)
                timer_reset = timer_reset.replace(hour=0, minute=1, second=0, microsecond=0)
            elif frequency == "Monthly":
                next_month = current_datetime.month + 1 if current_datetime.month < 12 else 1
                next_year = current_datetime.year if next_month > current_datetime.month else current_datetime.year + 1
                timer_reset = current_datetime.replace(year=next_year, month=next_month, day=1,
                                                                hour=0, minute=1, second=0, microsecond=0)
            elif frequency == "Yearly":
                timer_reset = current_datetime.replace(year=current_datetime.year + 1, month=1, day=1,
                                                                hour=0, minute=1, second=0, microsecond=0)
            else:
                print("Invalid frequency.")
                return

            # Update the last_done and streak fields in the habits table
            update_query = '''
            UPDATE habits SET last_done = ? WHERE habit_id = ?
            '''
            cursor.execute(update_query, (current_datetime, habit_id,))
            connection.commit()

            # Update the status of the habit to "Done"
            update_status_query = '''
            UPDATE habits SET status = ? WHERE habit_id = ?
            '''
            cursor.execute(update_status_query, ("Done", habit_id,))
            connection.commit()

            timer_reset = calculate_timer_reset(habit_id)
            deadline = calculate_deadline(habit_id)

            # Update the timer_reset of the habit
            update_timer_reset(habit_id, timer_reset)
            update_deadline(habit_id, deadline)

            current_date = current_datetime.strftime("%Y-%m-%d")

            print(f"Habit '{habit_name}' marked as done for {current_date}.")
                
            return habit_id
        else:
            print("This habit isn't due yet!")
            display_habits(user_id)
            what_to_do_now(user_id)

def calculate_streak(habit_id):
    """
    Calculates the streak of a habit and updates it in the database

    Parameters:
    habit_id (int): The ID of the habit

    Returns:
    int: The streak of the habit
    """
    select_query = '''
    SELECT * FROM habits WHERE habit_id = ?
    '''
    cursor.execute(select_query, (habit_id,))
    habit = cursor.fetchone()

    # Get the current status, last done, and streak of the habit    status = habit[10]
    last_done = habit[8]
    streak = habit[9]
    status = habit[10]

    # If the habit is done, calculate the streak
    if status == "Done":
        # Get the current date and time
        current_datetime = datetime.now()
        current_date = current_datetime.strftime("%Y-%m-%d")

        # Calculate the streak based on the last done date and time
        if last_done is not None:
            last_done_datetime = datetime.strptime(last_done, "%Y-%m-%d %H:%M:%S.%f")
            timer_reset = calculate_timer_reset(habit_id)
            if current_datetime <= timer_reset:
                if streak is not None:
                    streak = streak + 1
                else:
                    streak = 1

                    update_start_date_query = '''
                    UPDATE habits SET start_date = ? WHERE habit_id = ?
                    '''
                    cursor.execute(update_start_date_query, (current_date, habit_id,))
                    connection.commit()
                print("You're on a streak!")
            else:
                streak = 0
                print("You broke your streak!")

            # Update the streak in the habits table
            update_query = '''
            UPDATE habits SET streak = ? WHERE habit_id = ?
            '''
            cursor.execute(update_query, (streak, habit_id,))
            connection.commit()
    else:
        streak = 0

        # Update the streak in the habits table
        update_query = '''
        UPDATE habits SET streak = ? WHERE habit_id = ?
        '''
        cursor.execute(update_query, (streak, habit_id,))
        connection.commit()

    return streak, habit_id

def calculate_money_saved(habit_id):
    """
    Allows the user to see how much money they have saved by maintaining a streak

    Parameters:
    money_saved (int): The amount of money saved

    Returns:
    calculated_money_saved (int): The amount of money saved
    """
    select_query = '''
    SELECT * FROM habits WHERE habit_id = ?
    '''
    cursor.execute(select_query, (habit_id,))
    habit = cursor.fetchone()

    money_saved = habit[6]
    streak = habit[9]

    if money_saved is not None:
        calculated_money_saved = money_saved * streak
    else:
        money_saved = None

def calculate_time_saved(habit_id):
    """
    Allows the user to see how much time they have saved by maintaining a streak

    Parameters:
    time_saved (int): The amount of time saved

    Returns:
    calculated_time_saved (int): The amount of time saved
    """
    select_query = '''
    SELECT * FROM habits WHERE habit_id = ?
    '''
    cursor.execute(select_query, (habit_id,))
    habit = cursor.fetchone()

    time_saved = habit[7]
    streak = habit[9]
    
    if time_saved is not None:
        calculated_time_saved = time_saved * streak
    else:
        time_saved = None

def encouraging_message(habit_id):
    """
    Displays an encouraging message to the user after achieving a streak of 5 and in intervals of 5 after that

    Parameters:
    none

    Returns:
    none
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

    if streak == 5:
        print(encouraging_message)
    elif streak % 5 == 0:
        print(encouraging_message)
    else:
        None

def update_habit_status(user_id):
    """
    Checks and updates the status of habits based on the timer_reset and deadline

    Parameters:
    user_id (int): The ID of the user

    Returns:
    None
    """
    select_query = '''
    SELECT * FROM habits WHERE user_id = ?
    '''
    cursor.execute(select_query, (user_id,))
    habits = cursor.fetchall()

    for habit in habits:
        habit_id = habit[0]
        habit_name = habit[2]
        status = habit[10]
        timer_reset = habit[11]
        deadline = habit[12]
        streak = habit[9]

        # Get the current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Checks if the habit was done before the deadline, if not, the streak is reset and broken
        if current_datetime >= deadline:
            update_status_query = '''
            UPDATE habits SET status = ? AND streak = ? WHERE habit_id = ?
            '''
            cursor.execute(update_status_query, (None, 0, habit_id,))
            connection.commit()

            print(f"You broke your streak for habit '{habit_name}'!")
        else:
            # If the habit is done and the timer_reset has passed, update the status to "Not Done"
            if status == "Done" and current_datetime >= timer_reset:
                update_status_query = '''
                UPDATE habits SET status = ? WHERE habit_id = ?
                '''
                cursor.execute(update_status_query, ("Not Done", habit_id,))
                connection.commit()

                print(f"Habit '{habit_name}' is now due!")

            elif status == "Not Done" and current_datetime >= timer_reset:
                update_status_query = '''
                UPDATE habits SET status = ? AND streak = ? WHERE habit_id = ?
                '''
                cursor.execute(update_status_query, (None, 0, habit_id,))
                connection.commit()

                print(f"You broke your streak for habit '{habit_name}'!")
            
            else:
                None
    
def what_to_do_now (user_id):
    """
    Allows the user to choose what to do next	

    Parameters:
    choice (str): What the user chooses to do next

    Returns:
    none
    """
    while True:
        select_query = '''
        SELECT * FROM habits WHERE user_id = ?
        '''
        cursor.execute(select_query, (user_id,))
        habits = cursor.fetchall()

        print("What would you like to do?")
        print("1. Create a habit")
        print("2. Edit a habit")
        print("3. Delete a habit")
        print("4. View habit statistics")
        print("5. Mark habit as done")
        print("6. Exit")    
        choice = input("Enter your choice: ")

        if choice == "1":
            create_habits(user_id)
            display_habits(user_id)
        elif choice == "2":
            edit_habit(user_id)
            display_habits(user_id)
        elif choice == "3":
            delete_habit(user_id)
            display_habits(user_id)
        elif choice == "4":
            statistics(user_id)
        elif choice == "5":
            habit_id = mark_habit_done(user_id)
            calculate_streak(habit_id)
            calculate_money_saved(habit_id)
            calculate_time_saved(habit_id)
            encouraging_message(habit_id)
            display_habits(user_id)
        elif choice == "6":
            exit()
    