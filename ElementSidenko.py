class ElementSidenko:
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

# Create an element with atomic number 20 (Calcium)
element = ElementBikentaeva("Calcium", "Ca", 20)
element.dump()
