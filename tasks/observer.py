# Задача: Сделать систему, которой нужно будет объявлять что
# произошло нечто интересное не заботясь о том, кто получит уведомление.
# Например создать систему достижений, внеся незначительные изменения в 
# движок игры
from enum import Enum
from random import randint

class Event(Enum):
    EVENT_LEVEL_UP = 1

class Hero:
    def __init__(self):
        self.level = 0
        self.exp = 0

    def is_hero(self):
        return True

class NPC:
    def __init__(self):
        self.level = 0
        self.exp = 0

    def is_hero(self):
        return False

class Observer:
    def on_notify(self, entity, event):
        pass

class Achivments(Observer):

    @classmethod
    def on_notify(self, entity, event):
        if event == Event.EVENT_LEVEL_UP and entity.is_hero():
            print("Achivment complite, Level up")

class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, obs):
        self._observers.append(obs)

    def remove_observer(self, obs):
        self._observers.remove(obs)

    def notify(self, entity, event):
        for obs in self._observers:
            obs.on_notify(entity, event)

class Physics(Subject):
    def __init__(self):
        super().__init__()
        self.entites = [Hero(), NPC()]

    def update_level(self):
        for entity in self.entites:
            entity.exp += randint(0,5)
            if entity.exp > 10:
                entity.exp = 0
                entity.level += 1
                self.notify(entity, Event.EVENT_LEVEL_UP)

if __name__ == '__main__':
    physics = Physics()
    physics.add_observer(Achivments)
    for _ in range(5):
        physics.update_level()
        print('hero - ', physics.entites[0].level)
