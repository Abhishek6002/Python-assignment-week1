
from remove_duplicates import remove_duplicates


def test_remove_duplicates():
    assert remove_duplicates([4, 2, 4, 1, 2]) == [4, 2, 1]


def test_empty_list():
    assert remove_duplicates([]) == []


def test_no_duplicates():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]


def test_all_values_same():
    assert remove_duplicates([5, 5, 5]) == [5]


def test_preserves_order():
    assert remove_duplicates([3, 1, 2, 1, 3]) == [3, 1, 2]
