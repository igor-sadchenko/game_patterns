# TODO:
# 1. Необходимо упростить создание однотипных объектов. Необходимо избавиться от ввода начальных параметров.
# 2* Добавить к танкам WheeledVehicle с характеристиками hp=40, speed=80


class TankExample:

    def __init__(self, health, speed):
        self.health = health
        self.speed = speed


if __name__ == '__main__':
    allTanks = []

    allTanks.append(TankExample(health=30, speed=60))   # LightTank
    allTanks.append(TankExample(health=30, speed=60))
    allTanks.append(TankExample(health=100, speed=40))  # MediumTank
    allTanks.append(TankExample(health=100, speed=40))
    allTanks.append(TankExample(health=400, speed=20))  # HeavyTank
    allTanks.append(TankExample(health=400, speed=20))
