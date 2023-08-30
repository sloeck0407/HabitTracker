import pytest
import sqlite3
from unittest.mock import patch, mock_open
from tracking_data import create_table_test_habits, add_tracking_data
from step_by_step_habits import statistics
import re

@pytest.fixture
def setup_database():
    connection = sqlite3.connect(":memory:")  
    cursor = connection.cursor()
    
    cursor.execute(create_table_test_habits)
    add_tracking_data(1, connection, cursor)
    
    yield cursor  # Return cursor so tests can use it
    
    connection.close()

def test_statistics_habit_type_none(setup_database, capsys):
    cursor = setup_database  # Get the cursor from the fixture

    with patch('builtins.input', side_effect=['1', '1']):
        statistics(1, cursor)  # Pass the cursor to the statistics function
        
        captured = capsys.readouterr()
        print(captured.out)
        
        assert 'Select a habit type: ' in captured.out
        assert 'Health and Fitness' in captured.out

def test_statistics_habit_type(setup_database, capsys):
    cursor = setup_database  # Get the cursor from the fixture

    with patch('builtins.input', side_effect=['1', '5']):
        statistics(1, cursor)  # Pass the cursor to the statistics function
        
        captured = capsys.readouterr()
        print(captured.out)
        
        assert 'Select a habit type: ' in captured.out
        assert 'Mental and Emotional Well-Being' in captured.out

def test_statistics_habit_frequency_none(setup_database, capsys):
    cursor = setup_database  # Get the cursor from the fixture

    # Mock the input function to simulate user choices.
    with patch('builtins.input', side_effect=['2', '4']):
        # Call the statistics function
        statistics(1, cursor)
        
        # Capture the output
        captured = capsys.readouterr()
        print(captured.out)

        # Assert the presence of the expected print statement in the captured output.
        assert 'Select a frequency: ' in captured.out
        
        # Optionally, you can also check for the presence of other expected outputs.
        assert 'Yearly' in captured.out

def test_statistics_habit_frequency(setup_database, capsys):
    cursor = setup_database  # Get the cursor from the fixture

    # Mock the input function to simulate user choices.
    with patch('builtins.input', side_effect=['2', '2']):
        # Call the statistics function
        statistics(1, cursor)
        
        # Capture the output
        captured = capsys.readouterr()
        print(captured.out)

        # Assert the presence of the expected print statement in the captured output.
        assert 'Select a frequency: ' in captured.out
        
        # Optionally, you can also check for the presence of other expected outputs.
        assert 'Weekly' in captured.out
    
def test_statistics_run_streak_all_habits(setup_database, capsys):
    cursor = setup_database  # Get the cursor from the fixture
    
    # Mock the input function to simulate user choices.
    with patch('builtins.input', side_effect=['3']):
        # Call the statistics function
        statistics(1, cursor)
        
        # Capture the output
        captured = capsys.readouterr()
        print(captured.out)

        # Assert the presence of the expected print statements in the captured output.
        assert 'Meditate' in captured.out
        position_meditate = captured.out.index('Meditate')
        substring_after_meditate = captured.out[position_meditate:]
        assert '23' in substring_after_meditate, "Meditate should have a streak of 23"
        
        assert 'Clean Room' in captured.out
        position_clean_room = captured.out.index('Clean Room')
        substring_after_clean_room = captured.out[position_clean_room:]
        assert '5' in substring_after_clean_room, "Clean Room should have a streak of 5"
        
        assert 'Stop Eating Takeout' in captured.out
        position_stop_eating_takeout = captured.out.index('Stop Eating Takeout')
        substring_after_stop_eating_takeout = captured.out[position_stop_eating_takeout:]
        assert '4' in substring_after_stop_eating_takeout, "Stop Eating Takeout should have a streak of 4"

        assert 'Recycle' in captured.out
        position_recycle = captured.out.index('Recycle')
        substring_after_recycle = captured.out[position_recycle:]
        assert '1' in substring_after_recycle, "Recycle should have a streak of 1"

def test_statistics_run_streak_habit_type(setup_database, capsys):
    cursor = setup_database  # Get the cursor from the fixture
    
    # Mock the input function to simulate user choices.
    with patch('builtins.input', side_effect=['4', '1']):
        # Call the statistics function
        statistics(1, cursor)
        
        # Capture the output
        captured = capsys.readouterr()
        print(captured.out)

        # Assert the presence of the expected print statements in the captured output.
        assert 'Meditate' in captured.out
        position_meditate = captured.out.index('Meditate')
        substring_after_meditate = captured.out[position_meditate:]
        assert '23' in substring_after_meditate, "Meditate should have a streak of 23"


