import sqlite3
from datetime import datetime, timedelta
import pandas as pd
from tabulate import tabulate

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
    next_completion_time DATETIME,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
)
'''
cursor.execute(create_table_habits)

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

def break_habit():
    """
    Allows the user to choose the type of habit they wish to brake

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
        return break_habit()

def update_break_habit(habit_id):
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

def status(habit_id):
    """
    Allows the user to choose the status of their habit

    Parameters:
    status (str): The status of the habit

    Returns:
    none
    """
    print("Select habit status:")
    print("1. Done")
    print("2. Not Done")
    status_input = input("Enter your choice: ")

    if status_input == "1":
        status_input = "Done"
    elif status_input == "2":
        status_input = "Not Done"

    print("Your status is", status_input, "is that correct?")
    print("1. Yes")
    print("2. No")

    choice = input()
    if choice == "1":
        print("Perfect!")
        insert_data = '''
        INSERT INTO habits (status, habit_id)
        VALUES (?, ?)
        '''
        cursor.execute(insert_data, (status_input, habit_id,))
        connection.commit()

    elif choice == "2":
        status()

def get_time_limit(frequency):
    """
    Retrieves the time limit for streak based on the frequency

    Parameters:
    frequency (str): The frequency of the habit ("daily", "weekly", etc.)

    Returns:
    time_limit (int): The time limit in seconds
    """
    if frequency == "daily":
        return 24 * 60 * 60  # 24 hours in seconds
    elif frequency == "weekly":
        return 7 * 24 * 60 * 60  # 7 days in seconds
    elif frequency == "monthly":
        return 30 * 24 * 60 * 60 # 30 days in seconds
    elif frequency == "yearly":
        return 365 * 24 * 60 * 60 # 365 days in seconds
    else:
        return None

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
        last_done_input = datetime.now().strftime("%Y-%m-%d")

        insert_data = '''
        INSERT INTO habits (last_done, habit_id)
        VALUES (?, ?)
        '''
        cursor.execute(insert_data, (last_done_input, habit_id,))
        connection.commit()
    else:
        None

def streak(habit_id, frequency, status):
    """
    Calculates and updates the streak for a habit

    Parameters:
    habit_id (int): The ID of the habit
    frequency (str): The frequency of the habit
    status (str): The status of the habit

    Returns:
    None
    """
    if status == "Done":
        time_limit = get_time_limit(frequency)

        select_query = '''
        SELECT last_done FROM habits WHERE habit_id = ?
        '''
        cursor.execute(select_query, (habit_id,))
        last_done = cursor.fetchone()[0]

        if last_done is None:
            streak = 0
        else:
            streak = (datetime.now() - last_done).total_seconds() // time_limit

        #insert_data = '''
        #INSERT INTO habits (streak, habit_id)
        #VALUES (?, ?)
        #'''
        #cursor.execute(insert_data, (streak, habit_id,))
        #connection.commit()

        update_data = '''
        UPDATE habits SET streak = ? WHERE habit_id = ?
        '''
        cursor.execute(update_data, (streak, habit_id,))
        connection.commit()

    else:
        None
        
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
    print("Are you looking to break or create a habit?")
    print("1. Break a habit")
    print("2. Create a habit")
    choice = input("Enter your choice: ")
    if choice == "1":
    	habit_type_input, money_saved_input, time_saved_input = break_habit()
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
        print("Are you looking to break or create a habit?")
        print("1. Break a habit")
        print("2. Create a habit")
        choice = input("Enter your choice: ")
        if choice == "1":
            habit_type_input = update_break_habit(habit_id)
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
        exit()   

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
        exit()

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
        exit()

def calculate_streak(frequency, last_done):
    if last_done is None:
        return 0

    current_date = datetime.now().date()
    time_delta = current_date - last_done.date()

    if frequency == "Daily":
        return time_delta.days if time_delta.days <= 1 else 0
    elif frequency == "Weekly":
        return time_delta.days // 7 if time_delta.days <= 7 else 0
    elif frequency == "Monthly":
        return time_delta.days // 30 if time_delta.days <= 30 else 0
    elif frequency == "Yearly":
        return time_delta.days // 365 if time_delta.days <= 365 else 0
    else:
        return 0

def calculate_next_completion_time(frequency):
    """
    Calculates the next completion time based on the frequency

    Parameters:
    frequency (str): The frequency of the habit

    Returns:
    datetime: The calculated next completion time
    """
    current_datetime = datetime.now()

    if frequency == "Daily":
        next_completion_time = current_datetime + timedelta(days=1)
    elif frequency == "Weekly":
        days_until_next_weekday = (7 - current_datetime.weekday()) % 7
        next_completion_time = current_datetime + timedelta(days=days_until_next_weekday)
    elif frequency == "Monthly":
        next_month = current_datetime.month + 1 if current_datetime.month < 12 else 1
        next_year = current_datetime.year if next_month > current_datetime.month else current_datetime.year + 1
        next_completion_time = current_datetime.replace(year=next_year, month=next_month, day=1)
    elif frequency == "Yearly":
        next_completion_time = current_datetime.replace(year=current_datetime.year + 1, month=1, day=1)
    else:
        raise ValueError("Invalid frequency")

    next_completion_time = next_completion_time.replace(hour=0, minute=1, second=0, microsecond=0)
    return next_completion_time
    
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
    else:
        selected_habit = habits[habit_choice-1]
        habit_id = selected_habit[0]
        habit_name = selected_habit[2]
        frequency = selected_habit[4]

        # Get the current date and time
        current_datetime = datetime.now()

        # Calculate the next allowed completion time based on frequency
        if frequency == "Daily":
            next_completion_time = current_datetime + timedelta(days=1)
            next_completion_time = next_completion_time.replace(hour=0, minute=1, second=0, microsecond=0)
        elif frequency == "Weekly":
            days_until_next_weekday = (7 - current_datetime.weekday()) % 7
            next_completion_time = current_datetime + timedelta(days=days_until_next_weekday)
            next_completion_time = next_completion_time.replace(hour=0, minute=1, second=0, microsecond=0)
        elif frequency == "Monthly":
            next_month = current_datetime.month + 1 if current_datetime.month < 12 else 1
            next_year = current_datetime.year if next_month > current_datetime.month else current_datetime.year + 1
            next_completion_time = current_datetime.replace(year=next_year, month=next_month, day=1,
                                                            hour=0, minute=1, second=0, microsecond=0)
        elif frequency == "Yearly":
            next_completion_time = current_datetime.replace(year=current_datetime.year + 1, month=1, day=1,
                                                            hour=0, minute=1, second=0, microsecond=0)
        else:
            print("Invalid frequency.")
            return

        # Update the last_done and streak fields in the habits table
        update_query = '''
        UPDATE habits SET last_done = ?, streak = streak + 1 WHERE habit_id = ?
        '''
        cursor.execute(update_query, (current_datetime, habit_id,))
        connection.commit()

        # Update the next_completion_time in the habits table
        update_next_completion_query = '''
        UPDATE habits SET next_completion_time = ? WHERE habit_id = ?
        '''
        cursor.execute(update_next_completion_query, (next_completion_time, habit_id,))
        connection.commit()

        print(f"Habit '{habit_name}' marked as done for {current_datetime}. "
              f"Next completion time: {next_completion_time}.")

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
            mark_habit_done(user_id)
            display_habits(user_id)
        elif choice == "6":
            exit()
    