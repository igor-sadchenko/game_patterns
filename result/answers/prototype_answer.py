# Ключевой мыслью шаблона прототип является создание
# объекта, который может порождать объекты, похожие на себя
class Spawner:
    def __init__(self, prot):
        self.prototype = prot

    def spawnUnit(self):
        return self.prototype()


class TankPrototype:

    def __init__(self, health, speed):
        self.health = health
        self.speed = speed


class LightTank(TankPrototype):

    def __init__(self):
        super(LightTank, self).__init__(health=30, speed=60)


class MediumTank(TankPrototype):
    def __init__(self):
        super(MediumTank, self).__init__(health=100, speed=40)


class HeavyTank(TankPrototype):
    def __init__(self):
        super(HeavyTank, self).__init__(health=400, speed=20)


if __name__ == '__main__':
    LightTankSpawner = Spawner(LightTank)
    MediumTankSpawner = Spawner(MediumTank)
    HeavyTankSpawner = Spawner(HeavyTank)

    allTanks = []

    for _ in range(5):
        allTanks.append(LightTankSpawner.spawnUnit())
        allTanks.append(MediumTankSpawner.spawnUnit())
        allTanks.append(HeavyTankSpawner.spawnUnit())
