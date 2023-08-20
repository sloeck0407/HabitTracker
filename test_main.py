import pytest
import sqlite3
from unittest.mock import patch, mock_open
from tracking_data import create_table_test_habits, add_tracking_data
from step_by_step_habits import statistics

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
        assert 'Clean Room' in captured.out
        assert 'Stop Eating Takeout' in captured.out
        assert 'Recycle' in captured.out

        assert '23' in captured.out
        assert '5' in captured.out
        assert '4' in captured.out
        assert '2' in captured.out

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
        assert '23' in captured.out


