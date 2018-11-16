# TODO:
# 1. Необходимо упростить создание однотипных объектов. Необходимо избавиться от ввода начальных параметров.
# 2* Добавить к танкам WheeledVehicle с характеристиками hp=40, speed=80

import time


class TankExample:

    def __init__(self, health, speed):
        self.health = health
        self.speed = speed


def getTankByKey(strKey):
    if strKey == 'LightTank':
        time.sleep(20)
        return TankExample(health=30, speed=60)
    elif strKey == 'MediumTank':
        time.sleep(20)
        return TankExample(health=100, speed=40)
    elif strKey == 'HeavyTank':
        time.sleep(20)
        return TankExample(health=400, speed=20)


if __name__ == '__main__':
    allTanks = []

    allTanks.append(getTankByKey('LightTank'))
    allTanks.append(getTankByKey('LightTank'))
    allTanks.append(getTankByKey('MediumTank'))
    allTanks.append(getTankByKey('MediumTank'))
    allTanks.append(getTankByKey('HeavyTank'))
    allTanks.append(getTankByKey('HeavyTank'))
