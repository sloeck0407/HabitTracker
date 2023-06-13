import sqlite3
from datetime import datetime

# Connect to the SQLite database
connection = sqlite3.connect("habit_tracker.db")
cursor = connection.cursor()

# Create the users table if it doesn't exist
create_table_habits = '''
CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    habit_name TEXT,
    start_date DATETIME,
    frequency TEXT,
    habit_type TEXT,
    money_saved INTEGER,
    time_saved INTEGER,
    streak INTEGER,
    status TEXT
)
'''
cursor.execute(create_table_habits)

def display_habits(user_id):
    """
    Displays a table with all the habits of the user

    Parameters:
    user_id (int): The ID of the user

    Returns:
    None
    """
    # Retrieve the user's habits from the database
    select_query = '''
    SELECT * FROM habits WHERE user_id = ?
    '''
    cursor.execute(select_query, (user_id,))
    habits = cursor.fetchall()

    if not habits:
        print("You don't have any habits yet.")
    else:
        # Print the table header
        print("{:<10} {:<20} {:<15} {:<15} {:<15}".format(
            "Name", "Start Date", "Frequency","Streak", "Status"
        ))
        print("-" * 80)

        # Print each habit row
        for habit in habits:
            print("{:<10} {:<20} {:<15} {:<15} {:<15}".format(
                habit[3], habit[3], habit[5], habit[9], habit[10]
            ))

        print("-" * 80)

def habit_name():
    """
    Allows the user to create a name for their habit

    Parameters:
    name (str): The name of the habit

    Returns:
    none
    """
    habit_name_input = input("Name your habit!")

    print("The name of your habit is", habit_name_input, "is that correct?")
    print("1. Yes")
    print("2. No")

    while True:
        choice = input()
        if choice == "1":
            print("Perfect!")
            insert_data = '''
            INSERT INTO habits (habit_name)
            VALUES (?)
            '''
            cursor.execute(insert_data, (habit_name_input,))
            connection.commit()
            return
        elif choice == "2":
            habit_name()


def frequency():
    """
    Allows the user to select the frequency with which they wish to maintain the habit

    Parameters:
    choice (str): What the user chose as the frequency for the desired habit
    """
    print("Select habit frequency:")
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

    while True:
        choice = input()
        if choice == "1":
            print("Perfect!")
            insert_data = '''
            INSERT INTO habits (frequency)
            VALUES (?)
            '''
            cursor.execute(insert_data, (frequency_input,))
            connection.commit()
            return
        elif choice == "2":
            frequency()

def habit_type():
    """
    Allows the user to choose the type of habit they wish to create

    habit_type (str): The name of the type for the habit
    """
    def break_habit():
        print("You can choose one of the predifined typer or create your own!")
        print("1. Time Wasting")
        print("2. Money Wasting")
        print("3. Unhealthy")
        print("4. Other")
        choice = input("Enter your choice:")

        if choice == "1":
            habit_type_input = "Time Wasting"
        elif choice == "2":
            habit_type_input = "Time Wasting"
        elif choice == "3":
            habit_type_input = "Unhealthy"
        elif choice == "4":
            habit_type_input = input("Write your own type!")

        print("Your type is", habit_type_input, "is that correct?")
        print("1. Yes")
        print("2. No")

    while True:
        choice = input()
        if choice == "1":
            print("Perfect!")
            insert_data = '''
            INSERT INTO habits (habit_type)
            VALUES (?)
            '''
            cursor.execute(insert_data, (habit_type_input,))
            connection.commit()
            return
        elif choice == "2":
            frequency()

    def create_habit():
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
            habit_type = "Health and Fitness"
        elif choice == "2":
            habit_type = "Living and Organization"
        elif choice == "3":
            habit_type = "Learning and Personal Development"
        elif choice == "4":
            habit_type = "Relationships and Social Interactions"
        elif choice == "5":
            habit_type = "Mental and Emotional Well-Being"
        elif choice == "6":
            habit_type = "Environmental Sustainability"
        elif choice == "7":
            habit_type = input("Write your own type!")
        
        print("Your type is", habit_type, "is that correct?")
        print("1. Yes")
        print("2. No")

    while True:
        choice = input()
        if choice == "1":
            print("Perfect!")
            insert_data = '''
            INSERT INTO habits (habit_type)
            VALUES (?)
            '''
            cursor.execute(insert_data, (habit_type_input,))
            connection.commit()
            return
        elif choice == "2":
            frequency()

    print("Are you looking to break or create a habit?")
    print("1. Break a habit")
    print("2. Create a habit")

    while True:
        choice = input("Enter your choice: ")
        if choice in ["1", "2"]:
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    if choice == "1":
        break_habit()
    elif choice == "2":
        create_habit()




