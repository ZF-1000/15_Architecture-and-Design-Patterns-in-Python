class Observer:

    def update(self, subject):
        pass


class Subject:

    def __init__(self):         # набор наблюдателей
        self.observers = []

    def notify(self):
        """Уведомить всех наблюдателей об изменении состояния класса"""
        for item in self.observers:
            item.update(self)
