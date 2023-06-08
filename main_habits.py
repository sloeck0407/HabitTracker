from datetime import datetime
import pandas as pd
import sqlite3
from habit_tool import break_habit
from habit_tool import make_habit
from tabulate import tabulate
from database_user_registration import register
from database_user_registration import login

habits_broken = [
    break_habit("coffee", datetime(2023, 5, 24, 3, 51), cost_per_day=3, minutes_wasted=4)
   
]

df = pd.DataFrame(habits_broken)

print(tabulate(df, headers='keys', tablefmt='psql'))

habits_made = [
    make_habit("workout", "daily", datetime(2023, 1, 1, 12, 00), datetime.now(), status="not done")
]

df_1 = pd.DataFrame(habits_made)

print(tabulate(df_1, headers='keys', tablefmt='psql'))