from setuptools import setup, find_packages

setup(
    name='habittracker',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'datetime',
        'pandas',
        'tabulate',
        'pytest',
        'unittest.mock',
        'mock_open'
    ],  
    scripts=[
        'scripts/habit_tracker.py',
        'scripts/main_habits.py',
        'scripts/database_user_registration.py',
        'scripts/step_by_step_habits.py',
        'scripts/tracking_data.py',
        'scripts/test_main.py'
    ],  
    package_data={
        'habit_tracker': ['data/*.csv'],
    },  
    author='Sonia Vittoria Loeck',
)