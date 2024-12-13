class ElementRodnikov:
    def __init__(self, name, symbol, number):
        self.__name = name       
        self.__symbol = symbol   
        self.__number = number   

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def dump(self):
        """Выводит на экран значения атрибутов объекта"""
        print(f"Element Name: {self.name}")
        print(f"Symbol: {self.symbol}")
        print(f"Atomic Number: {self.number}")


# Создаем объект для элемента номер 19 — Калий (Potassium)
element = ElementBikentaeva("Potassium", "K", 19)
element.dump()
