# Ключевой мыслью шаблона прототип является создание
# объекта, который может порождать объекты, похожие на себя

import time


class TankExample:

    def __init__(self, health, speed):
        self.health = health
        self.speed = speed

    def clone(self):
        return TankExample(health=self.health, speed=self.speed)


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
    LightTank = getTankByKey('LightTank')
    MediumTank = getTankByKey('MediumTank')
    HeavyTank = getTankByKey('HeavyTank')

    allTanks = []

    allTanks.append(LightTank)
    allTanks.append(LightTank.clone())
    allTanks.append(MediumTank)
    allTanks.append(MediumTank.clone())
    allTanks.append(HeavyTank)
    allTanks.append(HeavyTank.clone())
