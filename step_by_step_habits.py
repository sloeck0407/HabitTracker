import sqlite3
from datetime import datetime

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
    FOREIGN KEY (user_id) REFERENCES users (user_id)
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

        elif choice == "2":
            habit_name()

    def frequency():
        """
        Allows the user to select the frequency with which they wish to maintain the habit

        Parameters:
        choice (str): What the user chose as the frequency for the desired habit

        Returns:
        none
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
                
            elif choice == "2":
                frequency()

    def habit_type():
        """
        Allows the user to choose the type of habit they wish to create

        Parameters:
        habit_type (str): The name of the type for the habit

        Returns:
        none
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
                habit_type_input = "Money Wasting"
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

                    print("Would you like to track how much money you save?")
                    print("1. Yes")
                    print("2. No")

                    while True: 
                        choice = input("Enter your choice: ")
                        if choice in ["1", "2"]:
                            break
                        else:
                            print("Invalid choice. Please enter a valid option.")
                        
                    if choice == "1":
                        money_saved_input = input("How much money will you save? ")
                    elif choice == "2":
                        money_saved_input = None  # Set money_saved to None if the user chooses not to track it

                    print("Would you like to track how much time you save?")
                    print("1. Yes")
                    print("2. No")

                    while True:
                        choice = input("Enter your choice: ")
                        if choice in ["1", "2"]:
                            break
                        else:
                            print("Invalid choice. Please enter a valid option.")
                        
                        if choice == "1":
                            time_saved_input = input("How much time will you save?(in minutes) " + "minutes")
                        elif choice == "2":
                            time_saved_input = None  # Set time_saved to None if the user chooses not to track it

                elif choice == "2":
                    habit_type()

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
                INSERT INTO habits (habit_type, habit_id)
                VALUES (?, ?)
                '''
                cursor.execute(insert_data, (habit_type_input, habit_id))
                connection.commit()

                money_saved = None
                time_saved = None

                insert_data = '''
                INSERT INTO habits (money_saved, time_saved, habit_id)
                VALUES (?, ?, ?)
                '''
                cursor.execute(insert_data, (money_saved, time_saved, habit_id,))
                connection.commit()

            elif choice == "2":
                habit_type()

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

        while True:
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
            last_done_input = datetime.now()

            insert_data = '''
            INSERT INTO habits (last_done, habit_id)
            VALUES (?, ?)
            '''
            cursor.execute(insert_data, (last_done_input, habit_id,))
            connection.commit()
        else:
            None

    def streak(habit_id, frequency):
        """
        Allows the user to track their streak

        Parameters:
        streak (int): The number of days the user has maintained their habit

        Returns:
        none
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

            insert_data = '''
            INSERT INTO habits (streak, habit_id)
            VALUES (?, ?)
            '''
            cursor.execute(insert_data, (streak, habit_id,))
            connection.commit()
        else:
            None

    select_query = '''
    SELECT * FROM habits WHERE user_id = ?
    '''
    cursor.execute(select_query, (user_id,))
    habits = cursor.fetchall()

    if not habits:
        print("You don't have any habits yet.")
        print("1. Create a habit")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            habit_name()
            frequency()
            habit_type()
            status(habit_id=habit_id)
            start_date(habit_id=habit_id)
            last_done(habit_id=habit_id)
            streak(habit_id=habit_id, frequency=frequency_input)

            insert_data = '''
            INSERT INTO habits (habit_name, frequency, habit_type, money_saved, time_saved, 
            status, start_date, last_done, streak, user_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            '''
            cursor.execute(insert_data, (habit_name_input, frequency_input, habit_type_input, 
            money_saved_input, time_saved_input,status_input, start_date_input, last_done_input, 
            streak, user_id,))
            connection.commit()

            print("Your habit has been created!")
            print("Here's a summary of your habit:")
            print("Habit name:", habit_name_input)
            print("Frequency:", frequency_input)
            print("Habit type:", habit_type_input)
            print("Status:", status_input)
            print("Start date:", start_date_input)
            print("Last done:", last_done_input)
            print("Streak:", streak)
        elif choice == "2":
            exit()
    else:
        select_query = '''
        SELECT * FROM habits WHERE habit_id = ?
        '''
        cursor.execute(select_query, (habit_id,))
        habits = cursor.fetchall()

        # Print the table header
        print("{:<10} {:<20} {:<15} {:<20} {:<10} {:<10} {:<20} {:<15} {:<15}".format(
            "Name", "Start Date", "Frequency", "Habit Type", "Money Saved", "Time Saved", 
            "Last Done", "Streak", "Status"
        ))
        print("-" * 120)

        # Print the table rows
        for habit in habits:
            print("{:<10} {:<20} {:<15} {:<20} {:<10} {:<10} {:<20} {:<15} {:<15}".format(
                habit[2], habit[3], habit[4], habit[5], habit[6], habit[7], 
                habit[8], habit[9], habit[10]
            ))
        print("-" * 120)

        """    
        print("1. Create a habit")
        print("2. Edit a habit")
        print("3. Delete a habit")
        print("4. View habit statistics")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            habit_name(habit_id = habit_id)
            frequency(habit_id = habit_id)
            habit_type(habit_id = habit_id)
            status(habit_id = habit_id)
            start_date(habit_id = habit_id)
            last_done(habit_id = habit_id)
            streak(habit_id = habit_id, frequency = frequency_input)

            print("Your habit has been created!")
            print("Here's a summary of your habit:")
            print("Habit name:", habit_name_input)
            print("Frequency:", frequency_input)
            print("Habit type:", habit_type_input)
            print("Status:", status_input)
            print("Start date:", start_date_input)
            print("Last done:", last_done_input)
            print("Streak:", streak)
        elif choice == "2":
        """
