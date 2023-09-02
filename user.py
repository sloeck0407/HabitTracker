from db import connect_to_db, create_user_table, insert_user, create_habits_table, insert_predefined_habits, fetch_habits, update_habit_field, delete_record
from habits import predefined_habits, display_habits

def register(cursor, connection, main_menu):
    """
    Allows a user to create a new account and register on the application

    Parameters:
    username (str): The user may choose a name for themselves
    email (str): The user will link their data to an email account
    password (str): The user will select a password to be able to access their account

    Returns:
    none
    """
    username = input("Enter a username: ")
    email = input("Enter an email address: ")
    password = input("Enter a password: ")

    select_data = '''
    SELECT * FROM users WHERE username = ? OR email = ?
    '''

    cursor.execute(select_data, (email, email))
    user = cursor.fetchone()

    if user:
        print("Seems like you already have an account. Try logging in!")
        main_menu(cursor, connection)
    else:
        insert_user(cursor, connection, username, email, password)
        user_id = cursor.lastrowid
        print("Registration successful!")
        create_habits_table(cursor)
        print("Seems like you're new here! Let's get started. These are some predefined habits, you can edit them, delete them and create your own too.")
        predefined_habits(user_id, cursor, connection)
        return user_id

def login(cursor, connection, main_menu):
    """
    Allows a user to log in to their account to access their data

    Parameters:
    login_input (str): The user enters their username or email
    password (str): The user enters their password

    Returns:
    If the password is correct: "Login successful!"
    If the password is incorrect: "Invalid username/email or password"
    """
    login_input = input("Enter your username or email: ")
    password = input("Enter your password: ")

    # Retrieve user information from the table
    select_query = '''
    SELECT * FROM users WHERE username = ? OR email = ?
    '''
    cursor.execute(select_query, (login_input, login_input))
    user = cursor.fetchone()

    if user and user[3] == password:
        print("Login successful!")
        user_id = user[0]
        return user_id
    else:
        print("Invalid username/email or password")

def delete_user(user_id, cursor, connection):
    """
    Deletes a user and all their associated habits.

    Parameters:
    user_id (int): The ID of the user to be deleted
    cursor (sqlite3.Cursor): The cursor object to execute SQL queries
    connection (sqlite3.Connection): The connection object to commit changes to the database

    Returns:
    None
    """

    print("Are you sure you want to delete this user?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Delete associated habits first (if there are any)
        delete_record("habits", "user_id", user_id, cursor)

        # Then delete the user
        delete_record("users", "user_id", user_id, cursor)

        # Commit changes to database
        connection.commit()

        print("User and associated habits have been deleted.")

    elif choice == "2":
        print("User was not deleted.")
