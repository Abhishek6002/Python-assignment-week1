from src.general_example import GeneralExample
from unittest.mock import patch

def test_flatten_dictionary():
    content = {
        "key1": [3, 2, 1],
        "key2": [42, 55, 10],
        "key3": [0, 22]
    }

    expected = [0, 1, 2, 3, 10, 22, 42, 55]

    actual = GeneralExample.flatten_dictionary(content)

    assert actual == expected

def test_flatten_dictionary_removes_duplicates():
    content = {
        "key1": [3, 2, 1],
        "key2": [2, 3, 4],
        "key3": [1, 5]
    }

    expected = [1, 2, 3, 4, 5]

    actual = GeneralExample.flatten_dictionary(content)

    assert actual == expected

def test_flatten_dictionary_empty_input():
    content = {}

    expected = []

    actual = GeneralExample.flatten_dictionary(content)

    assert actual == expected

def test_fetch_emp_details():
    with patch.object(
        GeneralExample,
        "load_employee_rec_from_database",
        return_value=["emp001", "Sam", "100000"]
    ):
        example = GeneralExample()
        actual = example.fetch_emp_details()

    expected = {
        "empId": "emp001",
        "empName": "Sam",
        "empSalary": "100000"
    }

    assert actual == expected