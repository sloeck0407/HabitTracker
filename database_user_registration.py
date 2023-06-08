import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("habit_tracker.db")
cursor = connection.cursor()

# Create the users table if it doesn't exist
create_table_user_data = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    password TEXT
)
'''
cursor.execute(create_table_user_data)

# User registration
def register():
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

    # Insert user information into the table
    insert_data = '''
    INSERT INTO users (username, email, password)
    VALUES (?, ?, ?)
    '''
    connection.commit()

    select_data = '''
    SELECT * FROM users WHERE username = ? OR email = ?
    '''

    cursor.execute(select_data, (email, email))
    user = cursor.fetchone()

    if user and user[2] == email:
        print("Seems like you already have an account. Try loging in!")
    else:
        print("Registration successful!")

def login():
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

    if user and user[3] == password:  # user[3] is the password column
        print("Login successful!")
        # Call a function to display the user's habits
        display_habits(user[0])  # user[0] is the id column
    else:
        print("Invalid username/email or password.")

# Main program loop
while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break

# Close the database connection
connection.close()
