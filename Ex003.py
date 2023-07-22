from time import time
from os import getlogin


class MyStr(str):
    """Данный класс расширяет класс str и добавляет в него новые функции"""
    def __new__(cls, text):
        """Расширение класса str"""
        instance = super().__new__(cls, text)
        instance.name = getlogin()
        instance.time = time()
        return instance


class Archive():
    """Данный класс архивирует свои экземпляры"""
    _nums = []
    _text = []

    def __init__(self, num, text):
        """Инициализация класса"""
        self._nums.append(num)
        self._text.append(text)

    def print_archive(self):
        """Метод, который выводит в терминал архив"""
        print(self._nums)
        print(self._text)


if __name__ == '__main__':
    help(MyStr)
    help(Archive)
