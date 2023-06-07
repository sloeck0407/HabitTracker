from datetime import datetime
from habit_tool import break_habit
from make_habit import make_habit
import pandas as pd
from tabulate import tabulate

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