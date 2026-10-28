
from squares import get_squares


def test_returns_20_squares():
    assert len(get_squares()) == 20


def test_first_square():
    assert get_squares()[0] == 1


def test_last_square():
    assert get_squares()[-1] == 400


def test_all_values_are_squares():
    assert get_squares() == [
        x * x for x in range(1, 21)
    ]
