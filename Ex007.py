class Matrix():
    """Класс Матрица"""
    def __init__(self, data):
        """Инициализация класса"""
        self.data = data

    def __eq__(self, other):
        """Операция сравнения матриц"""
        return self.data == other.data

    def print_matrix(self):
        """Вывод матрицы в терминал"""
        for i in range(len(self.data)):
            print(*self.data[i])

    def __add__(self, other):
        """Сложение матриц"""
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            print('Сложение невозможно!')
            return Matrix([[0], [0]])
        new_lis = self.data
        for i in range(len(self.data)):
            for k in range(len(self.data[i])):
                new_lis[i][k] = self.data[i][k] + other.data[i][k]
        return Matrix(new_lis)

    def __mul__(self, other):
        """Произведение матриц"""
        if len(self.data) != len(other.data[0]):
            print('Умножение невозможно!')
            return Matrix([[0], [0]])
        new_lis = [[0 for _ in range(len(other.data[0]))] for _ in range(len(self.data))]
        for i in range(len(self.data)):
            for j in range(len(other.data[0])):
                for k in range(len(other.data)):
                    new_lis[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(new_lis)
    
    def __str__(self):
        """Вывод информации в терминал для пользователя"""
        return f'Экземпляр класса Matrix с матрицей {self.data}'
    
    def __repr__(self):
        """Вывод информации в терминал для разработчика"""
        return f'Matrix({self.data})'


if __name__ == '__main__':
    lis = [[1, 2, 3, 4], [5, 6, 7, 8]]
    lis_2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    lis_3 = [[1, 2], [3, 4], [5, 6]]
    lis_4 = [[1, 2, 3], [4, 5, 6]]
    a = Matrix(lis)
    b = Matrix(lis_2)
    d = Matrix(lis_3)
    e = Matrix(lis_4)
    print(a.__eq__(b))
    a.print_matrix()
    c = a + b
    c.print_matrix()
    f = d*e
    f.print_matrix()

