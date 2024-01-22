import pytest
import csv
import tempfile
from utils import *
from scoreboard import *

def test_bubble_sort_dicts():
    data = [
        {"name": "John", "age": 30},
        {"name": "Jane", "age": 25},
        {"name": "Doe", "age": 35}
    ]
    key = "age"
    expected = [
        {"name": "Jane", "age": 25},
        {"name": "John", "age": 30},
        {"name": "Doe", "age": 35}
    ]
    assert bubble_sort_dicts(data, key) == expected


def test_write_data():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as csvfile:
        filename = csvfile.name

        # Call the function with test data
        write_data('test_name', 1, 'test_key', 'test_words')

        # Reset the file pointer to the beginning
        csvfile.seek(0)

        # Read the file and check its contents
        reader = csv.reader(csvfile)
        row = next(reader)
        assert row == ['test_name', '1', 'test_key', 'test_words']