class Archive():
    """Данный класс архивирует свои экземпляры"""
    _nums = []
    _text = []

    def __init__(self, num, text):
        """Инициализация класса"""
        self.num = num
        self.text = text
        self._nums.append(num)
        self._text.append(text)
    
    def __str__(self):
        """Вывод информации в терминал для пользователя"""
        return f'Экземпляр класса Archive с числом "{self.num}" и текстом "{self.text}"'
    
    def __repr__(self):
        """Вывод информации в терминал для разработчика"""
        return f'Archive({self.num}, {self.text})'

    def print_archive(self):
        """Вывод архива в терминал"""
        print(self._nums)
        print(self._text)


if __name__ == '__main__':
    a = Archive(7, 'Привет!')
    print(a.__str__())
    print(a.__repr__())