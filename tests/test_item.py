"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

def test_item():
    item = Item("стул", 100, 5)
    assert item.name == "стул"
    assert item.price == 100
    assert item.quantity == 5

    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 50

    item = Item("диван", 300, 15)
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 240

    item.name = "0123456789лишние_символы"
    assert item.name == "0123456789"
    item.name = "012345"
    assert item.name == "012345"
    item.name = ""
    assert item.name == "012345"
    assert Item.string_to_number("123") == 123
    print(len(Item.all))
    Item.instantiate_from_csv("src/items.csv")
    print(len(Item.all))
    assert Item.all[-1].name == "Клавиатура"

test_item()