from enum import Enum
from random import randint

class Event(Enum):
    EVENT_GET_DAMAGE = 1

class Tank:
    def __init__(self):
        self.hp = 100

class Observer:
    def on_notify(self, entity, event):
        raise NotImplemented

class DamageIndicator(Observer):
    @classmethod
    def on_notify(self, entity, event):
        if event == Event.EVENT_GET_DAMAGE:
            print("Draw red screen")

class HealthBar(Observer):
    @classmethod
    def on_notify(self, entity, event):
        if event == Event.EVENT_GET_DAMAGE:
            print("Set current health state to %d" % entity.hp)

class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, obs):
        self._observers.append(obs)

    def remove_observer(self, obs):
        self._observers.remove(obs)

    def notify(self, event):
        for obs in self._observers:
            obs.on_notify(event)

class Physics(Subject):
    def __init__(self):
        super().__init__()
        self.entites = [Tank()]

    def update_health(self):
        for entity in self.entites:
            if randint(0, 1):
                entity.hp = entity.hp - 1 if entity.hp > 0 else 0
                self.notify(entity, Event.EVENT_GET_DAMAGE)

if __name__ == '__main__':
    physics = Physics()
    physics.add_observer(HealthBar)
    physics.add_observer(DamageIndicator)
    for _ in range(5):
        physics.update_health()
        print('tank - ', physics.entites[0].hp)
