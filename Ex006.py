class Square ():
    """Класс прямоугольник"""
    def __init__(self, len_a=None, len_b=None, perimeter=None):
        """Инициализация класса"""
        if len_b == None:
            self.len_a = len_a
            self.len_b = len_a
        else:
            self.len_a = len_a
            self.len_b = len_b
        self.perimeter = perimeter

    def square_perimeter(self):
        """Расчёт периметра прямоугольника"""
        self.perimeter = round(2*self.len_a + 2*self.len_b, 2)

    def square_area(self):
        """Расчёт площади прямоугольника"""
        self.area = round(self.len_a*self.len_b, 2)

    def __add__(self, other):
        """Сложение периметров прямоугольников"""
        return Square(perimeter=self.perimeter + other.perimeter)

    def __sub__(self, other):
        """Вычитание периметров прямоугольника"""
        return Square(perimeter=abs(self.perimeter - other.perimeter))
    
    def __eq__(self, other):
        """Операция сравнения площадей прямоугольников"""
        return self.area == other.area

    def __ne__(self, other):
        """Операция сравнения площадей прямоугольников"""
        return self.area != other.area

    def __gt__(self, other):
        """Операция сравнения площадей прямоугольников"""
        return self.area > other.area

    def __ge__(self, other):
        """Операция сравнения площадей прямоугольников"""
        return self.area <= other.area
        
    def __lt__(self, other):
        """Операция сравнения площадей прямоугольников"""
        return self.area < other.area    

    def __le__(self, other):
        """Операция сравнения площадей прямоугольников"""
        return self.area >= other.area
    
    def __str__(self):
        """Вывод информации в терминал для пользователя"""
        return f'Экземпляр класса Square со сторонами {self.len_a} и {self.len_b}'
    
    def __repr__(self):
        """Вывод информации в терминал для разработчика"""
        return f'Square({self.len_a}, {self.len_b}, {self.perimeter}, {self.area})'

    def print_perimeter(self):
        """Вывод периметра в терминал"""
        return self.perimeter


if __name__ == '__main__':
    a = Square(10, 5)
    a.square_area()
    b = Square(5, 10)
    b.square_area()
    print(a.__eq__(b))
    print(a.__ne__(b))
    print(a.__gt__(b))
    print(a.__ge__(b))
    print(a.__lt__(b))
    print(a.__le__(b))