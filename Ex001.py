from time import time
from os import getlogin

class MyStr(str):
    """Класс строки"""
    def __new__(cls, text):
        """Инициализация класса"""
        instance = super().__new__(cls, text)
        instance.name = getlogin()
        instance.time = time()
        return instance
    
if __name__ == '__main__':
    a = MyStr('Привет!')
    print(a)
    print(a.name)
    print(a.time)