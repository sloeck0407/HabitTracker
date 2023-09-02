import sqlite3
from datetime import datetime, timedelta

def connect_to_db():
    connection = sqlite3.connect("habit_tracker.db")
    cursor = connection.cursor()
    return connection, cursor

def create_user_table(cursor):
    create_table_user_data = '''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT
    )
    '''
    cursor.execute(create_table_user_data)

def insert_user(cursor, connection, username, email, password):
    insert_data = '''
    INSERT INTO users (username, email, password)
    VALUES (?, ?, ?)
    '''
    cursor.execute(insert_data, (username, email, password))
    connection.commit()

def create_habits_table(cursor):
    create_table_habits = ''' 
    CREATE TABLE IF NOT EXISTS habits (
    habit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    habit_name TEXT,
    creation_date DATETIME,
    frequency TEXT,
    habit_type TEXT,
    money_saved INTEGER,
    time_saved INTEGER,
    last_done DATETIME,
    streak INTEGER,
    longest_streak INTEGER,
    status TEXT,
    timer_reset DATETIME,
    deadline DATETIME,
    accumulated_money_saved INTEGER,
    accumulated_time_saved INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
    '''
    cursor.execute(create_table_habits)

def insert_predefined_habits(user_id, predefined_habits, cursor, connection):
    insert_data = ''' 
    INSERT INTO habits (user_id, habit_name, creation_date, frequency, habit_type, money_saved, time_saved, status, last_done, streak)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    current_time = datetime.now()
    for habit in predefined_habits:
        cursor.execute(insert_data, (user_id, habit["habit_name"], current_time, habit["frequency"], habit["habit_type"], habit["money_saved"], habit["time_saved"], "Not Done", None, 0))
    connection.commit()

def save_new_habit(user_id, habit_name_input, creation_date, frequency_input, habit_type_input, money_saved_input, time_saved_input, cursor):
    """
    Saves the habit information into the table of habits

    Parameters:
    habit_name_input (str): The name of the habit
    creation_date (str): The date the habit was created
    frequency_input (str): The frequency of the habit
    habit_type_input (str): The type of the habit
    money_saved_input (int): The amount of money saved by the habit
    time_saved_input (int): The amount of time saved by the habit

    Returns:
    none
    """
    # Insert the habit into the habits table
    insert_data = '''
    INSERT INTO habits (user_id, habit_name, creation_date, frequency, habit_type, money_saved, time_saved, status, last_done, streak)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(insert_data, (user_id, habit_name_input, creation_date, frequency_input, habit_type_input, money_saved_input, time_saved_input, "Not Done", None, None))

def fetch_habits(user_id, cursor):
    """
    Fetches the habits from the table of habits

    Parameters:
    none

    Returns:
    habits (list): A list of habits
    """
    select_query = '''
    SELECT * FROM habits WHERE user_id = ?
    '''
    cursor.execute(select_query, (user_id,))
    return cursor.fetchall()
   
def update_habit_field(field_name, new_value, habit_id, cursor):
    """
    Updates the value of a field in the habits table

    Parameters:
    field_name (str): The name of the field to be updated
    new_value (str): The new value of the field
    habit_id (int): The id of the habit to be updated

    Returns:
    none
    """
    update_query = f'''
    UPDATE habits SET {field_name} = ? WHERE habit_id = ?
    '''
    cursor.execute(update_query, (new_value, habit_id))

def delete_record(table, column, value, cursor):
    """
    Deletes a record from a specified table based on a given condition.

    Parameters:
    table (str): The name of the table
    column (str): The column to be checked
    value (str|int): The value of the column
    cursor (sqlite3.Cursor): The cursor object to execute SQL queries

    Returns:
    None
    """
    delete_query = f'''
    DELETE FROM {table} WHERE {column} = ?
    '''
    cursor.execute(delete_query, (value,))

def fetch_habits_by_type(user_id, habit_type, cursor):
    """
    Fetch all habits of a specific type for a given user.

    Parameters:
    user_id (int): The ID of the user
    habit_type (str): The type of habit
    cursor (sqlite3.Cursor): The SQLite cursor

    Returns:
    A table of habit names and their types
    """
    select_query = '''
    SELECT * FROM habits WHERE user_id = ? AND habit_type = ?
    '''
    cursor.execute(select_query, (user_id, habit_type))
    return cursor.fetchall()   

def fetch_habits_by_frequency(user_id, frequency, cursor):
    """
    Fetch all habits of a specific frequency for a given user.

    Parameters:
    user_id (int): The ID of the user
    frequency (str): The frequency of habit
    cursor (sqlite3.Cursor): The SQLite cursor

    Returns:
    A table of habit names and their frequencies
    """
    select_query = '''
    SELECT * FROM habits WHERE user_id = ? AND frequency = ?
    '''
    cursor.execute(select_query, (user_id, frequency))
    return cursor.fetchall()

def fetch_longest_streaks(user_id, longest_streak, cursor):
    """
    Fetch the longest streaks for all habits of a given user.

    Parameters:
    user_id (int): The ID of the user
    longest_streak (int): The longest streak of habit
    cursor (sqlite3.Cursor): The SQLite cursor

    Returns:
    A table of habit names and their longest streaks
    """
    select_query = '''
    SELECT habit_name, longest_streak FROM habits WHERE user_id = ?
    '''
    cursor.execute(select_query, (user_id,))
    longest_streaks = cursor.fetchall()

    # Create a DataFrame from the habits data
    columns = ["Name", "Longest Streak"]
    habit_data = []
    for habit in longest_streaks:
        # Check for None values and substitute with an empty string or placeholder
        habit_name = habit[0] if habit[0] is not None else ""
        longest_streak = habit[1] if habit[1] is not None else ""

        habit_data.append([habit[0], habit[1]])

    habit_df = pd.DataFrame(habit_data, columns=columns)

    # Display the DataFrame as a formatted table
    table = tabulate(habit_df, headers='keys', tablefmt='psql')
    print(table)

def fetch_longest_streak_for_habit(user_id, habit_id, longest_streak, cursor):
    """
    Fetch the longest streak for a given habit of a given user.

    Parameters:
    user_id (int): The ID of the user
    habit_id (int): The ID of the habit
    longest_streak (int): The longest streak of habit
    cursor (sqlite3.Cursor): The SQLite cursor

    Returns:
    Dict: A dictionary of habit names and their longest streaks
    """
    select_query = '''
    SELECT habit_name, longest_streak FROM habits WHERE user_id = ? AND habit_id = ?
    '''
    cursor.execute(select_query, (user_id, habit_id))
    longest_streaks = cursor.fetchall()

    # Create a DataFrame from the habits data
    columns = ["Name", "Longest Streak"]
    habit_data = []
    for habit in longest_streaks:
        # Check for None values and substitute with an empty string or placeholder
        habit_name = habit[0] if habit[0] is not None else ""
        longest_streak = habit[1] if habit[1] is not None else ""

        habit_data.append([habit[0], habit[1]])

    habit_df = pd.DataFrame(habit_data, columns=columns)

    # Display the DataFrame as a formatted table
    table = tabulate(habit_df, headers='keys', tablefmt='psql')
    print(table)

def update_accumulated_fields(cursor, habit_id, money_saved=None, time_saved=None):
    """
    Updates the accumulated money and time saved fields for a given habit.

    Parameters:
    cursor (sqlite3.Cursor): The SQLite cursor
    habit_id (int): The ID of the habit
    money_saved (int): The amount of money saved by the habit
    time_saved (int): The amount of time saved by the habit

    Returns:
    None
    """
    # Get the current values of the accumulated money and time saved fields
    select_query = '''
    SELECT accumulated_money_saved, accumulated_time_saved FROM habits WHERE habit_id = ?
    '''
    cursor.execute(select_query, (habit_id,))
    current_values = cursor.fetchone()
    current_money_saved = current_values[0] if current_values[0] is not None else 0
    current_time_saved = current_values[1] if current_values[1] is not None else 0

    # Check if money_saved and time_saved are provided and add them to the current values
    new_money_saved = current_money_saved + (money_saved if money_saved is not None else 0)
    new_time_saved = current_time_saved + (time_saved if time_saved is not None else 0)

    # Update the accumulated money and time saved fields
    update_query = '''
    UPDATE habits SET accumulated_money_saved = ?, accumulated_time_saved = ? WHERE habit_id = ?
    '''
    cursor.execute(update_query, (new_money_saved, new_time_saved, habit_id))

def update_timer_reset_and_deadline(cursor, habit_id, timer_reset, deadline):
    """
    Updates the timer reset and deadline fields for a given habit.

    Parameters:
    cursor (sqlite3.Cursor): The SQLite cursor
    habit_id (int): The ID of the habit
    timer_reset (datetime): The date and time the timer was reset
    deadline (datetime): The deadline for the habit

    Returns:
    None
    """
    # Update the timer reset and deadline fields
    update_query = '''
    UPDATE habits SET timer_reset = ?, deadline = ? WHERE habit_id = ?
    '''
    cursor.execute(update_query, (timer_reset, deadline, habit_id))

def update_streak(cursor, habit_id, streak):
    """
    Updates the streak field for a given habit.

    Parameters:
    cursor (sqlite3.Cursor): The SQLite cursor
    habit_id (int): The ID of the habit
    streak (int): The current streak of the habit

    Returns:
    None
    """
    # Update the streak field
    update_query = '''
    UPDATE habits SET streak = ? WHERE habit_id = ?
    '''
    cursor.execute(update_query, (streak, habit_id))

def update_status_and_streak(cursor, connection, habit_id, status, streak):
    cursor.execute('UPDATE habits SET status = ?, streak = ? WHERE habit_id = ?', (status, streak, habit_id,))
    connection.commit()

def update_status(cursor, connection, habit_id, status):
    cursor.execute('UPDATE habits SET status = ? WHERE habit_id = ?', (status, habit_id,))
    connection.commit()

