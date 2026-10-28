
import pytest

from person import Person, Male, Female


def test_male_gender():
    assert Male().get_gender() == "Male"


def test_female_gender():
    assert Female().get_gender() == "Female"


def test_person_is_abstract():
    with pytest.raises(TypeError):
        Person()
