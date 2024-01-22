import pytest
import csv
import tempfile
import io
import sys
#from main import *
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
        write_data('test_name', 1, 'test_key', 'test_words', filename)

        # Reset the file pointer to the beginning
        csvfile.seek(0)

        # Read the file and check
        reader = csv.reader(csvfile)
        row = next(reader)
        assert row == ['test_name', '1', 'test_key', 'test_words']


def test_read_data():
    # Create a temporary file and write some test data to it
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['test_name', '1', 'test_key', 'test_words'])
        filename = csvfile.name

    # Call the function and get the csv reader
    csvreader = read_data(filename)

    # Read the first row from the csv reader
    row = next(csvreader)
    assert row == ['test_name', '1', 'test_key', 'test_words']
