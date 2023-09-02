from db import connect_to_db, create_user_table, create_habits_table
from user import register, login, delete_user
from habits import predefined_habits, display_habits, create_habits, edit_habit, delete_habit, statistics, mark_habit_done, calculate_and_update_streak, encouraging_message, update_habit_status

def main_menu(cursor, connection):
    '''
    This function displays the main menu of the application.

    Parameters:
    cursor (sqlite3.Cursor): The cursor object to execute SQL queries
    connection (sqlite3.Connection): The connection object to commit changes to the database

    Returns:
    none
    '''
    print("Welcome to the Habit Tracker App!")
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice: ")

    if choice == "1":
        user_id = register(cursor, connection, main_menu)
        if user_id is not None:
            display_habits(user_id, cursor)
            post_login_menu(user_id, cursor)

    elif choice == "2":
        user_id = login(cursor, connection, main_menu) 
        if user_id is not None:
            update_habit_status(user_id, cursor, connection)
            display_habits(user_id, cursor)
            post_login_menu(user_id, cursor)
    else:
        print("Invalid choice.")

def post_login_menu(user_id, cursor):
    '''
    This function displays the menu after the user has logged in or registered successfully.
    
    Parameters:
    user_id (int): The user's unique id
    cursor (sqlite3.Cursor): The cursor object to execute SQL queries

    Returns:
    none
    '''
    while True:
        print("What would you like to do?")
        print("1. Create a habit")
        print("2. Edit a habit")
        print("3. Delete a habit")
        print("4. View habit statistics")
        print("5. Mark habit as done")
        print("6. Delete user account")
        print("7. Exit")    
        choice = input("Enter your choice: ")

        if choice == "1":
            create_habits(user_id, cursor, connection)
            display_habits(user_id, cursor)
        elif choice == "2":
            edit_habit(user_id, cursor, connection)
            display_habits(user_id, cursor)
        elif choice == "3":
            delete_habit(user_id, cursor, connection)
            display_habits(user_id, cursor)
        elif choice == "4":
            statistics(user_id, cursor,connection)
        elif choice == "5":
            habit_id = mark_habit_done(user_id, cursor, connection)
            if habit_id is not None:
                calculate_and_update_streak(habit_id, cursor, connection)
                encouraging_message(user_id, habit_id, cursor)
                display_habits(user_id, cursor)
        elif choice == "6":
            delete_user(user_id, cursor, connection)
            break
        elif choice == "7":
            break

if __name__ == "__main__":
    connection, cursor = connect_to_db()
    create_user_table(cursor)
    main_menu(cursor, connection)  # Start the app with the main menu

