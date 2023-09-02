# My Habit Tracker App
An application designed to help users build and maintain their habits, track their progress, and see how much money and time they're saving with each habit.

## Features
* Registration: Create a new user or login to an existing one
* Habit Management: Create, edit, delete and check off habits
* Streaks: Keep track of your streaks and see your longest streak
* Data Analysis: See your habits by regularity or type, as well as your longest streak

## Installing

### Using Git
Clone this repository
```bash
git clone https://github.com/sloeck0407/HabitTracker.git
```
Navigate to the project directory
```bash
cd HabitTracker
```
Create virtual environment
```bash
python3.10 -m venv myvenv
```
Activate virtual environment
```bash
myvenv\Scripts\activate
```
Install the requirements
```bash
pip install -r requirements.txt
```
Run the app
```bash
python3 main.py
```

### Downloading the zip
Download the zip file from [here](https://github.com/sloeck0407/HabitTracker) and extract it.
Create virtual environment
```bash
python3.10 -m venv myvenv
```
Activate virtual environment
```bash
myvenv\Scripts\activate
```
Install the requirements
```bash
pip install -r requirements.txt
```
Run the app
```bash
python3 main.py
```

## Getting Started
### Create a user
When you run the app, you will be able to register or signup to an account using a username, email and inputing a password. You can create as many users as you want, and you can switch between them at any time.

### Create a habit
Once you have created a user, you will automatically start  out with 5 habits, which you can later delete or edit. You can also create your own habits. You will be able to choose the regularity of the habit (daily, weekly, monthly or yearly), whether it's a habit to overcome or create a new habit and whether you want to track how much money and time you will save. 

### Check off a habit
You can mark a habit as done by choosing which habit has been done typing the number for the desired habit, which will increase the streak by one. If you miss a day, the streak will be reset to 0. Every 5th day of having completed the habit, you will be able to see a motivational quote.

### Analyze your data
You can analyze your data by choosing typing the number for the desired habit. You will be able to see your longest streak (for every or for a given habit) and your habits by regularity or type. 

## Built With
* [Python](https://www.python.org/) - Programming language
* [SQLite](https://www.sqlite.org/index.html) - Database
* [Pytest](https://docs.pytest.org/en/stable/) - Testing

## Testing
To run the tests, run the following command in the terminal
```bash
pytest
```
This will run all the test cases included in the project. If the tests are successful, you will see a message indicating the number of passed tests. If any tests fail, pytest will provide details on what went wrong.

