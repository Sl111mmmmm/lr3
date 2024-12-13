import math

class ConeBase:
    team_info = "Команда разработчиков: Родников Родион - разработчик 1, Сиденко Григорий - разработчик 2"
    
    @staticmethod
    def about():
        return ConeBase.team_info
    
    def __init__(self, radius, height):
        self.__radius = radius
        self.__height = height

    def set_radius(self, radius):
        """Метод для установки радиуса основания"""
        self.__radius = radius

    def set_height(self, height):
        """Метод для установки высоты"""
        self.__height = height

    def get_radius(self):
        """Метод для получения радиуса основания"""
        return self.__radius

    def get_height(self):
        """Метод для получения высоты"""
        return self.__height

class Cone(ConeBase):
    def __init__(self, radius, height):
        super().__init__(radius, height)

    def calculate_surface_area(self):
        """Метод для расчета площади поверхности конуса"""
        radius = self.get_radius()
        height = self.get_height()
        slant_height = math.sqrt(radius**2 + height**2) 
        return math.pi * radius * (radius + slant_height) 

try:
    r = float(input("Введите радиус основания конуса: "))
    h = float(input("Введите высоту конуса: "))
    
    if r > 0 and h > 0:
        cone = Cone(r, h)
        print("Радиус основания конуса:", cone.get_radius())
        print("Высота конуса:", cone.get_height())
        print("Площадь поверхности конуса:", cone.calculate_surface_area())
        print(ConeBase.about())
    else:
        print("Радиус и высота должны быть положительными числами.")
except ValueError:
    print("Попробуйте еще раз и введите корректное числовое значение.")
