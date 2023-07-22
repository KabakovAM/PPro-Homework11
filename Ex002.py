class Archive():
    """Данный класс архивирует свои экземпляры"""
    _nums = []
    _text = []

    def __init__(self, num, text):
        """Инициализация класса"""
        self._nums.append(num)
        self._text.append(text)

    def print_archive(self):
        """Вывод архива в терминал"""
        print(self._nums)
        print(self._text)


if __name__ == '__main__':
    a = Archive(7, 'Привет!')
    b = Archive(2, 'Пока!')
    a.print_archive()
