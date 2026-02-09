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

    print(item.all)
    print(item.all[0].price)

test_item()