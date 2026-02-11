from pathlib import Path
import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name != "":
            self.__name = new_name[0:10]
        else:
            print("Ошибка, пустая строка!")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        current_dir = Path(__file__).parent
        project_root = current_dir.parent
        file_path = project_root / 'src' / 'items.csv'
        with open(file_path, "r") as file:
            for i in (csv.DictReader(file)):
                cls(i.get("name"), i.get("price"), i.get("quantity"))

    @staticmethod
    def string_to_number(str_number):
        try:
            return int(str_number)
        except ValueError:
            print("Ошибка строка не является числом!")
