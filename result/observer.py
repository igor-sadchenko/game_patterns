# Задача: Упростить и сделать возможным добавление других обработчиков урона
# без изменения класса Physics.


class Tank(object):
    def __init__(self):
        self.hp = 100


class DamageIndicator():

    def set_red_screen(self):
        print("Draw red screen")


class HealthBar(object):

    def update_healt_bar(self, entity):
        print("Set current health state to %d" % entity.hp)


class Physics(object):
    def __init__(self):
        super().__init__()
        self.entites = [Tank()]
        self.damageIndicator = DamageIndicator()
        self.healthBar = HealthBar()

    def damageAll(self):
        for entity in self.entites:
            entity.hp = entity.hp - 1 if entity.hp > 0 else 0
            if self.damageIndicator:
                self.damageIndicator.set_red_screen()
            if self.healthBar:
                self.healthBar.update_healt_bar(entity)


if __name__ == '__main__':
    physics = Physics()
    for _ in range(5):
        physics.damageAll()
        print('tank - ', physics.entites[0].hp)