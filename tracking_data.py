import sqlite3
import datetime

connection = sqlite3.connect("test_habits.db")
cursor = connection.cursor()

create_table_test_habits = '''
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
    accumulated_time_saved INTEGER
)
'''
cursor.execute(create_table_test_habits)

user_id = 1

def add_tracking_data(user_id, connection, cursor):
    """
    Add tracking data for predefined habits for testing
    !!! This function is only for testing purposes !!!
    """
    # Add tracking data for test user 1
    insert_data = '''
    INSERT INTO habits (user_id, habit_name, creation_date, frequency, habit_type, money_saved, time_saved, last_done, streak, longest_streak, status, timer_reset, deadline, accumulated_money_saved, accumulated_time_saved)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(insert_data, (user_id, "Meditate", datetime.datetime(2023, 7, 1), "Daily", "Mental and Emotional Well-Being", 0, 0, datetime.datetime(2023, 7, 23), 23, 23, 
    "Not Done", datetime.datetime(2023, 7, 24), datetime.datetime(2023, 7, 25), 0, 0))
    cursor.execute(insert_data, (user_id, "Clean Room", datetime.datetime(2023, 7, 1), "Weekly", "Living and Organization", 0, 0, datetime.datetime(2023, 7, 22), 4, 5, 
    "Done", datetime.datetime(2023, 7, 24), datetime.datetime(2023, 7, 30), 0, 0))
    cursor.execute(insert_data, (user_id, "Stop Eating Takeout", datetime.datetime(2023, 7, 3), "Weekly", "Money Wasting", 30, 0, datetime.datetime(2023, 7, 13), 2, 4, 
    "Not Done", datetime.datetime(2023, 7, 17), datetime.datetime(2023, 7, 23), 180, 0))
    cursor.execute(insert_data, (user_id, "Recycle", datetime.datetime(2023, 7, 1), "Monthly", "Environmental Sustainability", 0, 0, datetime.datetime(2023, 7, 1), 1, 1, 
    "Done", datetime.datetime(2023, 8, 1), datetime.datetime(2023, 8, 31), 0, 0))
    connection.commit()

add_tracking_data(user_id, connection, cursor)
connection.close()
