from datetime import datetime
import pandas as pd
from tabulate import tabulate
import sqlite3
from database_user_registration import register, login
from step_by_step_habits import habit_name, frequency, habit_type, display_habits

connection = sqlite3.connect("habit_tracker.db")
cursor = connection.cursor()

create_table_user_data = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    password TEXT
)
'''
cursor.execute(create_table_user_data)

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
            display_habits(user_id)
    elif choice == "3":
        break

display_habits(user_id)

connection.close()