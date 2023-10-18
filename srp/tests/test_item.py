import pytest

from srp.item import Item


def test_initial_state_item():
    item = Item()
    assert item.get_value() == 0
    assert item.get_description() == ''


@pytest.mark.parametrize(
    "description, expected",
    [
        ("Wood Chair", "Wood Chair"),
        ("TV led", "TV led")
    ]
)
def test_correct_get_set_item_description(description, expected):
    item = Item()
    assert item.set_description(description=description) is True
    assert item.get_description() == expected


def test_wrong_data_type_set_item_description():
    item = Item()
    assert item.set_description(description=123) is False


def test_correct_get_set_item_value():
    item = Item()
    assert item.set_description(description='Wood Chair') is True
    assert item.get_description() == 'Wood Chair'


def test_wrong_data_type_set_item_value():
    item = Item()
    assert item.set_value(value='123') is False


def test_valid_item():
    item = Item()
    item.set_description('Wood Chair')
    item.set_value(123.00)
    assert item.validate() is True


def test_invalid_item():
    item = Item()
    item.set_description('')
    item.set_value(0)
    assert item.validate() is False


def test_item_without_value():
    item = Item()
    item.set_description(description='Wood Chair')
    assert item.validate() is False


@pytest.mark.parametrize(
    "invalid_item",
    [
        11, 2222, 23.00
    ]
)
def test_item_whitout_description(invalid_item):
    item = Item()
    item.set_value(value=invalid_item)
    assert item.validate() is False






