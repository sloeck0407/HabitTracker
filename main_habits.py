from datetime import datetime
import pandas as pd
from tabulate import tabulate
import sqlite3
from database_user_registration import register, login
from step_by_step_habits import predefined_habits, create_habits, display_habits, edit_habit, update_habit_status, what_to_do_now

connection = sqlite3.connect("habit_tracker.db")
cursor = connection.cursor()

create_table_user_data = '''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    password TEXT
)
'''
cursor.execute(create_table_user_data)

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

# Main program loop
while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        user_id = login()                
        if user_id is not None:
            select_query = '''
            SELECT * FROM habits WHERE user_id = ?
            '''
            cursor.execute(select_query, (user_id,))
            habits = cursor.fetchall()
            if not habits:
                print("Seems like you're new here! Let's get started. These are some predefined habits, you can edit them, delete them and create your own too.")
                predefined_habits(user_id)  # Call the function to create predefined habits
                display_habits(user_id)  # Call the function to display habits
            else:
                update_habit_status(user_id)  # Call the function to update habit status
                display_habits(user_id) 

        what_to_do_now(user_id)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Try again.")

# Close the database connection
connection.close()