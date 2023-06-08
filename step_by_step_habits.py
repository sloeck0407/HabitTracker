import sqlite3
import datetime

# Connect to the SQLite database
connection = sqlite3.connect("habit_tracker.db")
cursor = connection.cursor()

# Create the users table if it doesn't exist
create_table_habits = '''
CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    habit_name TEXT,
    periodicity TEXT,
    habit_type TEXT,
    streak INTEGER,
    start_date DATETIME,
    money_saved INTEGER,
    time_saved INTEGER,
    status TEXT
)
'''
cursor.execute(create_table_habits)

def habit_name():
    """
    """
    name = input("Name your habit!")

    print("The name of your habit is", name, "is that correct?")
    print("1. Yes")
    print("2. No")

    while True:
        choice = input()
        if choice == "1":
            print("Perfect!")
        elif choice == "2":
            habit_name()

def periodicity():
    """
    
    """
    print("Select habit frequency:")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    print("4. Yearly")
    choice = input("Enter your choice: ")

    if choice == "1":
        choice = "Daily"
    elif choice == "2":
        choice = "Weekly"
    elif choice == "3":
        choice = "Monthly"
    elif choice == "4":
        choice = "Yearly"

    print("Your periodicity is", choice, "is that correct?")
    print("1. Yes")
    print("2. No")

    while True:
        choice = input()
        if choice == "1":
            print("Perfect!")
        elif choice == "2":
            periodicity()

def habit_type():
    """
    """
    def break_habit():
        print("You can choose one of the predifined typer or create your own!")
        print("1. Time Wasting")
        print("2. Money Wasting")
        print("3. Unhealthy")
        print("4. Other")
        choice = input("Enter your choice:")

        if choice == "1":
            habit_type = "Time Wasting"
        elif choice == "2":
            habit_type = "Time Wasting"
        elif choice == "3":
            habit_type = "Unhealthy"
        elif choice == "4":
            habit_type = input("Write your own type!")

        print("Your type is", habit_type, "is that correct?")
        print("1. Yes")
        print("2. No")

        while True:
            choice = input()
            if choice == "1":
                print("Perfect!")
            elif choice == "2":
                break_habit()

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
            elif choice == "2":
                break_habit()

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
