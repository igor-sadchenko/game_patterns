# Задача: Сделать систему, которой нужно будет объявлять что
# произошло нечто интересное не заботясь о том, кто получит уведомление.
# Например создать систему повреждений, внеся незначительные изменения в 
# движок игры

from enum import Enum
from random import randint

class Tank:
    def __init__(self):
        self.hp = 100

class DamageIndicator():

    def set_red_screen(self):
        print("Draw red screen")

class HealthBar():

    def update_healt_bar(self, entity):
        print("Set current health state to %d" % entity.hp)

class Physics(Subject):
    def __init__(self):
        super().__init__()
        self.entites = [Tank()]
        self.damageIndicator = DamageIndicator()
        self.healthBar = HealthBar()

    def update_health(self):
        for entity in self.entites:
            if randint(0, 1):
                entity.hp = entity.hp - 1 if entity.hp > 0 else 0
                if self.damageIndicator:
                    self.damageIndicator.set_red_screen()
                if self.healthBar:
                    self.healthBar.update_healt_bar(entity)

if __name__ == '__main__':
    physics = Physics()
    for _ in range(5):
        physics.update_health()
        print('tank - ', physics.entites[0].hp)