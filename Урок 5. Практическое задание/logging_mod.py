from reusepatterns.singletones import SingletonByName
import time


# Заметка, можно применить стратегию если добавить стратегию логирования
class Logger(metaclass=SingletonByName):

    def __init__(self, name):
        self.name = name

    def log(self, text):
        print('log--->', text)


# декоратор
def debug(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('DEBUG-------->', 'Функция: ', func.__name__, 'Выполнялась: ', end - start)
        return result

    return inner
